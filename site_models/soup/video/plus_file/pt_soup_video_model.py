__author__ = 'Vit'
from bs4 import BeautifulSoup

from base_classes import UrlList
from loader.base_loader import URL,FLData
from loader.request_load import RequestLoad
from setting import Setting
from site_models.base_site_model import ParseResult, ControlInfo, ThumbInfo, FullPictureInfo
from site_models.soup.base_soup_model import BaseSoupSite, _iter
from site_models.util import quotes


class PTvideoSoupSite(BaseSoupSite):
    def start_button_name(self):
        return "PTvid"

    def get_start_button_menu_text_url_dict(self):
        return dict(All_Videos=URL('http://www.porntrex.com/videos?t=a*'),
                    Added_Today=URL('http://www.porntrex.com/videos?t=t*'),
                    Added_This_Week=URL('http://www.porntrex.com/videos?t=w*'),
                    Added_Tis_Month=URL('http://www.porntrex.com/videos?t=m*'),
                    Photo_Most_Recent=URL('http://www.porntrex.com/albums?o=mr*'),
                    Photo_Most_Photos=URL('http://www.porntrex.com/albums?o=mp*'),
                    Photo_Top_Rated=URL('http://www.porntrex.com/albums?o=tr*'),
                    Photo_Most_Viewed=URL('http://www.porntrex.com/albums?o=mv*')
                    )

    def startpage(self):
        return URL("http://www.porntrex.com/videos*")

    def can_accept_index_file(self, base_url=URL()):
        return base_url.contain('porntrex.com/')

    def parse_thumbs(self, soup: BeautifulSoup, result: ParseResult, base_url: URL):
        for thumbnail in _iter(soup.find_all('div', {'class': 'thumb-overlay'})):
            href = URL(thumbnail.parent.attrs['href'], base_url=base_url)
            description = thumbnail.img.attrs['alt']
            thumb_url = URL(thumbnail.img.attrs['data-original'], base_url=base_url)

            duration = thumbnail.find('div', {'class': 'duration'}).contents[-1]
            dur_time = '' if duration is None else str(duration.string).strip()

            hd_div = thumbnail.find('div', {'class': 'hd-text-icon'})
            hd = '' if hd_div is None else str(hd_div.string).strip()

            result.add_thumb(ThumbInfo(thumb_url=thumb_url, href=href, popup=description,
                                       labels=[{'text': dur_time, 'align': 'top right'},
                                               {'text': description, 'align': 'bottom center'},
                                               {'text': hd, 'align': 'top left', 'bold': True}]))

    def parse_thumbs_tags(self, soup: BeautifulSoup, result: ParseResult, base_url: URL):
        for tags_container in _iter(soup.find_all('div', {'class': 'btn-group'})):
            if tags_container is not None:
                for tag in _iter(tags_container.find_all('a')):
                    result.add_control(ControlInfo(str(tag.string), URL(tag.attrs['href'], base_url=base_url)))

    def get_pagination_container(self, soup: BeautifulSoup) -> BeautifulSoup:
        return soup.find('ul', {'class': 'pagination'})

    def parse_video(self, soup: BeautifulSoup, result: ParseResult, base_url: URL):
        wrapper = soup.find('div', {'id': 'wrapper'})
        if wrapper is not None:
            script = wrapper.find('script', text=lambda x: 'SWFObject(' in str(x))
            if script is not None:
                config_xml_url = URL(quotes(str(script.string), '?config=', '"'), base_url=base_url)
                # print(config_xml_url)
                result.set_video()
                result.set_waiting_file()
                self.model.request_file(FLData(config_xml_url,''),lambda filedata:self.continue_parse_video(filedata,result))

    def continue_parse_video(self, filedata:FLData, result:ParseResult):
        bs = BeautifulSoup(filedata.text, 'html.parser')
        files = bs.find_all(lambda tag: tag.name.startswith('file'))
        urls = UrlList()
        for item in _iter(files):
            urls.add(item.name, URL(item.string, base_url=filedata.get_url()))

        result.set_video(urls.get_media_data(-1))
        self.model.on_file_parsed(filedata,result)


    def parse_video_tags(self, soup: BeautifulSoup, result: ParseResult, base_url: URL):
        # adding user to video
        user_container = soup.find('table', {'class': 'user-tab'})
        username_span = user_container.find('span')
        href = URL(username_span.parent.attrs['href'] + '/videos', base_url=base_url)
        username = str(username_span.string)
        result.add_control(ControlInfo(username, href, text_color='blue'))

        # adding tags to video
        for item in _iter(soup.find_all('div', {'class': 'catmenu'})):
            for href in _iter(item.find_all('a')):
                if href.string is not None:
                    result.add_control(ControlInfo(str(href.string), URL(href.attrs['href'], base_url=base_url)))

    def parse_pictures(self, soup: BeautifulSoup, result: ParseResult, base_url: URL):
        photo_container = soup.find('div', {'class': 'panel-body'})
        if photo_container is not None:
            s1, s2, s3 = photo_container.find_all('span', recursive=False)
            num_of_photos = int(s3.string)
            first = photo_container.find('img')
            href_first = str(first.attrs['data-original']).replace('/tmb/', '/')
            part = href_first.rpartition('/')
            first_num = int(part[2].partition('.')[0])
            ext = part[2].partition('.')[2]

            base_dir = base_url.get_path(base=Setting.base_dir)
            result.set_gallery_path(base_dir)

            for number in range(first_num, first_num + num_of_photos):
                name = str(number) + '.' + ext
                url = URL(part[0] + '/' + name, base_url=base_url)
                picture = FullPictureInfo(abs_href=url, rel_name=name)
                picture.set_base(base_dir)
                result.add_full(picture)


if __name__ == "__main__":
    pass
