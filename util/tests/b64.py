# -*- coding: utf-8 -*-
__author__ = 'Vit'

import re


def base64decode(txt):
    base64 = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/="
    output = ""
    i = 0

    txt1 = ""

    invalid = re.compile('[^A-Za-z0-9+/=]')
    for ch in txt:
        # print(ch, invalid.match(ch))
        if invalid.match(ch) is None:
            txt1 += ch

    while i < len(txt1):
        enc1 = base64.find(txt1[i])
        enc2 = base64.find(txt1[i + 1])
        enc3 = base64.find(txt1[i + 2])
        enc4 = base64.find(txt1[i + 3])

        ch1 = (enc1 << 2) | (enc2 >> 4)
        ch2 = ((enc2 & 15) << 4) | (enc3 >> 2)
        ch3 = ((enc3 & 3) << 6) | enc4

        output += chr(ch1)
        if enc3 != 64:
            output += chr(ch2)
        if enc4 != 64:
            output += chr(ch3)

        i += 4

    return output


if __name__ == "__main__":
    txt = "UEhOamNtbHdkQ0JzWVc1bmRXRm5aVDBpU21GMllWTmpjbWx3ZENJZ2RIbHdaVDBpZEdWNGRDOXFZWFpoYzJOeWFYQjBJajRLWm5WdVkzUnBiMjRnWkdoWllYTTJNemhJS0dsdWNIVjBLU0I3Q2lBZ2RtRnlJR0poYzJVMk5DQTlJQ0pCUWtORVJVWkhTRWxLUzB4TlRrOVFVVkpUVkZWV1YxaFpXbUZpWTJSbFppSWdLd29nSUNBZ0ltZG9hV3ByYkcxdWIzQnhjbk4wZFhaM2VIbDZNREV5TXpRMU5qYzRPU3N2UFNJN0NpQWdkbUZ5SUc5MWRIQjFkQ0E5SUNJaU93b2dJSFpoY2lCamFERXNJR05vTWl3Z1kyZ3pMQ0JsYm1NeExDQmxibU15TENCbGJtTXpMQ0JsYm1NME93b2dJSFpoY2lCcElEMGdNRHNLSUFvZ0lHbHVjSFYwSUQwZ2FXNXdkWFF1Y21Wd2JHRmpaU2d2VzE1QkxWcGhMWG93TFRrckx6MWRMMmNzSUNJaUtUc0tJQ0JrYnlCN0NpQWdJQ0JsYm1NeElEMGdZbUZ6WlRZMExtbHVaR1Y0VDJZb2FXNXdkWFF1WTJoaGNrRjBLR2tyS3lrcE93b2dJQ0FnWlc1ak1pQTlJR0poYzJVMk5DNXBibVJsZUU5bUtHbHVjSFYwTG1Ob1lYSkJkQ2hwS3lzcEtUc0tJQ0FnSUdWdVl6TWdQU0JpWVhObE5qUXVhVzVrWlhoUFppaHBibkIxZEM1amFHRnlRWFFvYVNzcktTazdDaUFnSUNCbGJtTTBJRDBnWW1GelpUWTBMbWx1WkdWNFQyWW9hVzV3ZFhRdVkyaGhja0YwS0drckt5a3BPd29nQ2lBZ0lDQmphREVnUFNBb1pXNWpNU0E4UENBeUtTQjhJQ2hsYm1NeUlENCtJRFFwT3dvZ0lDQWdZMmd5SUQwZ0tDaGxibU15SUNZZ01UVXBJRHc4SURRcElId2dLR1Z1WXpNZ1BqNGdNaWs3Q2lBZ0lDQmphRE1nUFNBb0tHVnVZek1nSmlBektTQThQQ0EyS1NCOElHVnVZelE3Q2lBS0lDQWdJRzkxZEhCMWRDQTlJRzkxZEhCMWRDQXJJRk4wY21sdVp5NW1jbTl0UTJoaGNrTnZaR1VvWTJneEtUc0tJQW9nSUNBZ2FXWWdLR1Z1WXpNZ0lUMGdOalFwSUc5MWRIQjFkQ0E5SUc5MWRIQjFkQ0FySUZOMGNtbHVaeTVtY205dFEyaGhja052WkdVb1kyZ3lLVHNLSUNBZ0lHbG1JQ2hsYm1NMElDRTlJRFkwS1NCdmRYUndkWFFnUFNCdmRYUndkWFFnS3lCVGRISnBibWN1Wm5KdmJVTm9ZWEpEYjJSbEtHTm9NeWs3Q2lBS0lDQWdJR05vTVNBOUlHTm9NaUE5SUdOb015QTlJQ0lpT3dvZ0lDQWdaVzVqTVNBOUlHVnVZeklnUFNCbGJtTXpJRDBnWlc1ak5DQTlJQ0lpT3dvZ0NpQWdmU0IzYUdsc1pTQW9hU0E4SUdsdWNIVjBMbXhsYm1kMGFDazdDaUFLSUNCeVpYUjFjbTRnYjNWMGNIVjBPd3A5Q21SdlkzVnRaVzUwTG5keWFYUmxLR1JvV1dGek5qTTRTQ2hrYUZsaGN6WXpPRWdvSWxWRlpGTmpSMUp3VVc1Q1lWSkVRbkJaZWs1TFlXeG5lbHBJYkZwWFJVcHRWVlpTUW1Wck1YRmFNM0JPWVcxa05WTlhiRU5sYlZKSllraE9ZVlpFUW5CWGEyUnpaVzFPU0dWSGFHeFdTRUl4V1dwSk1XSkZiSEZPVlZab1YwVTFiMWRYTVRSaVJXeEpZa2hhYTFkRmJHNVZWbVJUWVZkS1NFOVhjR2hsVlVwU1dXdG9WMkp0UmxoT1IyUmhZbFJzTlZOVmFHdGhSMUpJVkcwNVNsTkdTblpYYkU1RFRXMUdXRlZ0ZUdsbGJtUXlWMnRrYzAxc1FuRmxSM1JvVjBac2JsbFdaRkpQVld4MVZHNXNXazFVYTNwWk1qRkhaREZvTmxGWWNFNWhiVTEzVkZod2NtVlZNVFZUVTNSUlVqSjRkRmt5TVVka1JuQlVVVzV3YW1KVk1EVlRWekZ2VFVkU1NWRnVjRkJoVkdneVdXcE9RMkpIU25SbFNGcGFWakZHTVZkVVNUUmtiSEJZVFZkc1lWWXhSakpWYlhoVFZqSldTRnBHVm1wbGEwcGFWR3hTYm1ScmJIQlJibkJhVFRCd01sbHJaRFJqUjBwMFdYcHNTbUpVVmpKVFYyeERZbGRPZEZKdVVtRldNSEF5V1RJeFUySkhUbkZOUjJ4T1VUQnNibHBFU25OaE1sSklXbnBzU21Gc2JETlVWVTVLV2pKR1NGWnVRbUZOYldkM1ZVWk9TbVZyTlVWUlYyeEtVakJhZWxscll6Vk5NWEIxVm01T2FWTkZOWEZaTWpGWFlrZEtjVTFIYkd0VFJXOTRWMnhPU2xveVVYbFdiV3hvVFcxM2QxZFdaRFJqTWtsNldrY3hhMVl6YUhwWmVrcFBaVlp3V0ZadVZsRlZNRzkzV1RJMVYySkZiSEJSYmxKcFRUTkNiMWxyWkRSa2JWRjVWMnBHYVZJemFEWlhWRTVMWWtad1dFNUViRXBpYkVvMVdrWmtWbUZXUW5Ga00xcG9WakZ3TlZkV1kzaGlSa0p4WkROYVlWSXlkM2xWUjJSMlV6Qk9ibUl3ZEVSYU1qbE1WVVZPUm1SRmVGUlJiRVpwVFRCS1ExZHJhRTVrVjBwMFZtcENTbEpyU2pKWk1HaFhaRlp3U0ZadWJFcFNWVFV5VjJ0a1Zsb3hjSFJQV0d4S1UwZFJlbHBJYXpGbGJWSkpVMjE0V2xaNlJuSlhiR1JoWWtkS2RGUnRlRTFpVlRVeVdXeE9RbVJGZUZWT1JYUlJVMFUxY1ZreU1YTmtNbEpFVVdwQ2JGZEZTbk5WUms1TFRVWndXV0ZFUWsxTmJrSnZXa2N4UjJWc2EzcFRia0pxVTBaR2NGVkhaSFphTUd4SlYyMW9hbUZWU20xWk1HTTFaREJzUlUxSFpGbE5NRW95V1RCT1EwOUhXa1JSYlVwWlZraE9URk5WVGtOYWJVNUlUMWhrVFdKclNYaFpla3B1WWpGa05WcEljR2hYUmtwelZURmtVbUpyZUVSUldHaE9Va1pWZUZSclVrcGxWbWhVWVhwa1JHRlZSbTVYUkU1RFpHMU9SRTVZWkd0WFJUVjJVekJhZW1KdFNsaGlTRlpTWWxkNGNsTnViRE5hTURGRVRraGtUbEpGUmpOVVZWSkRXa1YwVldNd2RFcFJNRXB0V1RCak5XUXdlSFZSYWtacVRXMWtkbFl6Ykd0a01rbDZVV3BHYVdKV1NuTlpNalZQVlZad1dWTnJjRlpSTWs1NlUxVlNRMXBGZEZWak1IUktVVEJLYlZrd1l6VmtNSGgxVVdwR2FrMXRaSFpXTTJ4cllURndXR1ZIYUd4V1ZYQnpXa1ZvYTJKR2NGaE9SelZOVVRCR00xZEdUbkpPTUU1d1VWZGtXVTB3U2pKWk1FMHhaREpTV1ZSdE9VeFNiazUxVjJ0a1YySldiRmxXYms1clVUSk9lbE5WWkdGaFIwcEpWRzE0V1ZVeWN6TlJNbXhDV2pGbmVsRnVXbXBSZWxZeldrWm9UMkl3ZEVkak1qVmhVakZhZEZkV2FGZGpNbEpIVVcxNGFtRXhTbTlhVms1cVl6QnNSVkZ0VWt4V1NFNU1VMVZPUTFwdFRraFBXR1JOWW10SmVGbDZTbTVpTVdRMVdrUkNhVTB3U2pCWmFrNVBUVVpTU0ZKcVZtRlhSV3gxVkVWT1EySldiRmhsU0hCaFZtcENkMVF6WkhaYU1HeEVZVWN4YTFaNlZuRmFSV1J6WkcxS2NGb3pRa3BUU0U1TVUxVk9RbG93YkVsWGJXaHFZVlZLTTFkV1RrSlBWV3hJVlc1YVdrMHhXakJYYkdNeFRVVjRkRlJ1YkdGV01GbDNWMnhXVjJNeGNGaE5WM2hwWW14R2RsTnFUazloYlU1MFlraGthMUV5VG5kVU0yeERaREZzVkU1VVFteFhSVXB6VTFWUmQxb3diM3BWYlhoc1UwWkdNbGxYTVVkTmJHeFpWRzF3YW1KWGVETmFSVTVxVGpCc1NWRnRhRTFpVlZvMldsWmpNV0ZyYkVWTlIyUnJVMFZ2ZUZkc1VucFRNR3hFVVZka1NsTkdjRzlaTW14RFpXdHNSVTFIWkdGU2VteHhXa1pqZUdKSFNuVlZXRlpoVFd4WmQxVnNaRFJpUjBwWVZtNVdhMU5GTlVSYVZscFRZVVp2ZDA1WGFHbFdNVloyVTJwT1QyRnRUblJpU0dSclVUSk9kMVl6Y0VOYVJUazFVVlYwU2xFd1JtNVRWV2hEWVVWNGRWUnViRnBsVlVVMVUxVk9hbVJyZDNsVVdHaE5ZbXRLTWxrd1pFZGhNazQxVGxoV1lWZEdSakpaTUdNMVpEQjRkR05JY0V0bGJrNU1VMVZPUWxvd2JFbFJiV2hOWWxSc01WZHNhRXRsVjBsNlUxZGtVVlV3U25SYVJtTXhZVzFTU0dKSVdtbGhWMlIzVTFWb2VsTXdiRVJSVjJSS1VUQkdibHBITVVkbFZXeEpWRzFvU2xKRVFtNVhhMk0xWVcxU1dFMVhlR2xpYkVZeFYxUk9TMkpHYkZsVmJYaFRWak5vYzFsc1pGZGtWMUpFV2pJMWFrMXJOVFZaVm1oRFRVVndOV0Y2WkVwVFJUVnZWRWMxVTA1WFRraFdWMlJSVlRCR2RWcEZaRmRPUjFKRVQxaEdXbGRHY0c5WmVrcFBaVmRHV1ZGcVFrdGxiazV1V1hwS1JtUldiRmxVYWxacFlsVXhibFZHVGtOTlIwNTFWbTE0VUdReU9XNVRWVTVDV2pCc1JGRnVjRnBWZWxZMldUSXhUbG94UWxSUlZ6Vk5aVlJzY1ZSWGF6RmtNa2w2VVcxb1lWTkZNVEZaYlRGWFRVVjNlbEZ1V21wUmVsWjRXVE5zYWs0d1RuQlJWMlJLVVRCR2JsTlZhRTVrVjA1SVVtNXNZVlo2VlhkV1J6QTFZVEZ3VkU1WVFtbGlhelZ6V1RJMVUxRXhjRmhYYmxwcVlsWldkbGw2U2taak1HeEpWRmhDVUdReU9XNVRWVTVDV2pKYVZXTXdkRXBSTUVadVUxVm9UbVJYVGtoU2JteGhWbnBWZDFaSE1EVmhNWEJVVGxoQ2FXSnJOWE5aTWpWVFVURndXRmR1V21waVZsWjJXVEJrUm1Nd2JFbFVXRUpRWkRJNWJsTlZaM2RqUlhSRVlYcGtSR0Z1WkRKWmVrcFBaVmRHV1ZGcVFsRmFNamcwVTFaTmQyUkZiRWRSYmxwcVVsVmFjbGt6YXpGa1ZuQlpWVmRrVmxKNmJETmFSbU14WVRGd1dWTlhaRkpOYW14eVYyeE9RMUp0U25SVlYyUk5WWHBCY2xFeVpIWmFNR3hGWkRKb1RWVjZRbTVWTUdSelpXMVNTRkpxUW1wbFZGWnhXV3BKZDFvd2JFZFViRlpTVm10d1ZsTlZUa0ppTVd4WllraFdXbVZYZERCVVJsRXdVekZDU1ZSdGNHcGlWM2d6V2tWT1EwMUhWbGxSYlhoUlZUQnZkMWRzYUc5TlJYZDVZMGRvYTJKVldqWlhWRTVMWTBkT1NWVlhiRkZpYkhCdldUSnNRMXBzVGtoU2JuQnNWbnBXY1ZWR1RrTmFiRTVJVW01d2JGWjZWbkZhYTJneldqRmplRTFFWkVSaVJHeEtWMVpvVDA1WFNuUlVXRlpxVTBaYU5sbFZUbTlaYTI5M1lVaENhazB4U205YVJXaE9aRmROZWxWdGFHcGliRVoxVkVWT1FtSnJNVlJrTTNCT1pXeEdORlJXVW1wTlZYaEZWVmhPVGxFelpETlVSVkpDWXpBeFJWRllaRTVXUlVZelZGVlNRbUpzYUZSaGVtUkVZa1JzU2xkV2FFOU9WMHAwVkZoV2FsTkdXalpaVlU1dldXdHZkMkZJUW1wTk1VcHZXa1ZvVG1SV2NIUlNibkJvVlRKT2VsTlZUbXBsUlc5NFRVaENVR1F6UW0xVk1HUkhaVzFXV0U1WGNFMWlhMGw0V1hwS2JtSXhaRFZhUld4b1YwVTBkMWRXYUZObGEzaDFWVzVzV2xZd05YbFhSRXB2WTBkU1NWUlhOVTFSTUVaMVUycEZkMk5GT1ROaU1qbGhZbXhhTVZkVVRsTmpSMGw1VGtjNVRGVXdTVE5STWpWaFlVZE9jRkZ0T1dwbFZVVTFVMVZrVTJSc2EzcFdibEpoVm5wVmQxUkhNVTlsVm5CWVVtcENZVlpXV25wWGJHTjRZa2RLZFZWWE9VdE5NRFZ4V1RJeGMyUXlVa1JaTTBKUVpWVktkbGt6YXpGTlIxWlpVVzE0U2xKRVFtNVRhazVUWWtkV1NWVllXbWhpVlZsNVYxWm9UMkZ0VG5SaVNHUnJVVEpOTTFOVlpHOWxhM2gwVW01d2JGWjZWbkZUVlZGM1dqSlNTVk5xUm1GV1NFNU1XVlZvVG1SWFRYcFRiWEJLVWtSQ2JsTXdUbXRpTWxKSlZXNWtVR0ZVYURKWk0zQkdaREI0ZEdGSVFtcE5NVXB2V2tWb1RtUldhM2xQV0ZKTlRXNUNObFJXVWxkYWJHeFpWRmhXYUdKck1YVlRNVko2VXpCMFNGVnVXbHBOTVZvd1YyeGpNVTFGZUhSYVIzaHJVbFphZWxkc1kzaGlSMHAxVlc1d1VtSnRlRlpYVm1SclZERnNXRTFYZUV4Uk1sSjJWMnhrUjJFd2NEVmlSMHBPVW1wQ2JscHJhRE5hTVhCSVQxZHdhMVo2Um5OWmJUVlNaRlp2ZVZacVFsTldNMmh6V1d4a1YyUlhVa2xVYTA1c1ZteEtiMWRxUVRGaFIwcFlWbGM1UzAxcmNESlhhMmh5WW10MFYyTXpaRmxWTW5ReFYxWm9RMlF4Y0ZoT1YzUlNUVzFvZDFsclpGSmlNa1pKVkZoQ1VHUXpRVFZUTVU1dVkwVTVObVF6V21wTmF6VTFXVlpvUTAxR1FtNWllbWhwWWxSc05sZFVUa3RqUjA1SlZWTjBVVkl3Vm01WlZXaExZa1p3Y1UxSGJHaFRSa2wzV1RCU2RtUnJkM3BhUkU1clpWUldkbGxXYUU5TlJteFpWVzV3VFdKVk5USlpiRTVLV2pKU1NGSnViR0ZOYkZsM1ZVWk9TMXBzYkhSbFIyaHBZbGhPY0ZWSGNEUmpSMHBZV1RKa1NsTkZOVFZYV0c5M1lWZEdTVlZxUW1wU1J6a3lWRVJPVDJWdFVraFNha0pvVmpBeE5GUkhNVzlqUjAxNlZXMW9hMU5GTVRGWFZFazFaRVY0TmxGWVZtRk5iWGgwVlVod1RtVnJOVVZTV0doUFpXeFdkRlJXVWtKbFJXeHdVVzFvYVZOR1JUVlRWekZQWkcxU1dFNVVRbUZYUld4dVdYcE9VMkZIVWtsVVYyeEtVakJ3TWxreU1WTmlSMDV4VFVkc1RsRXdhM0pWUlUwMVlVWkNjV1F6V21saVZHdzJWMVJPUzJOSFRrbFZVM1JFWVc1a2IxUkdUWGRhTVU1SVlraHdhMUl3V1hkWk0yc3hZVzFKZVUxSFpFcFNWbHBRVld0T1Fsb3dlRlJOUTNSRVdqSTVURkV5WkhaUFJuQklZa1JLU2xORk5IZGFWbVEwWWtaQ1ZGTnRNV2xOYWxWM1ZFWm9UMk5IVm5SV1ZGcFFWMFZKTUZRemJFTmtNV3hZVlcxMGFGWjZWblZVTW5CQ1dqQXhkVkZxVWxCTk1Fb3lXWHBLYzAxSFJsaFBXRlpRWVZWS2RGbFdhRzlpUm5CRlpFUkNhVTB3UlRKVVZsSldUakpPZEdKSE5XaFRSa1V5VkZWU01FNXJlRmhpU0ZaaFVqRlpNRlF5Y0Vaa01ERkZVVlJrYTFJeFdUQmFSVTE0WVVkS1NHSkhOV2xoYmtKeFYyeGpNVTFHY0ZsVFZHUmFZbFZhY1ZsVVNtdGxWMGw2Vm01V1lWRjZSbkZaYWtvMFpHMU9jV0l5Y0ZwaGJFWXpWRlpTUW1WRk9IbFVibHBwVW5wc05WUXliRTlpVm5CMFYxUmthVTB3U205WFZFcHpUVWRXVldJelpFMWhiV016VTFkdk1WVlhUblJQVkVKaFZqQTBkMWRzWkZKYU1sRjVZa1JDYUZFd1JUUlhWazVEWlcxU1NXSklUbUZXUkVKd1YxUkpOV015U1hwVFZGcEtUV3h3ZEZkdGJFcGFNa1pKVTIxNFlXRnFRbkJaVldoVFRVZE9SV0l6V2sxTk1sRjZXa2hyTVdWdFVrbFRiWGhhVm5wR2NsZHNaR0ZpUjBwMFZHMTRUV0pWTlRKWmJFMDFZMGRLZEZWdGVHeFJlbFl6V1ZWb1FtRlZiRWxWYldocVlsZFNjMXBGVVhkaFZtZDVVMjVPV2xaNlZubFRWMnhEVFVkR1dWVnVUbUZXUkVKd1UxZHZNVlpIVWtsVGJYaGFWbnBDYmxWclpGZGlWbkJZVGxkd1lWWklaREpYVmxFd1QwVjNlVlZ1UW10aGFsSk1VVEp3TkdFeVJsbFhWMlJvVmpGRk5WTlhOVTlOUjA1MFZtMW9hVlY2Um5CWFZtTXhaRlp3V1ZOWGJFcFRSVFIzV2xaa05HSkdRbFJUYm1ScFRUQTFkMXBGWkhOa2JVcHhZakprWVdKWGR6QlhiR1JTVGpKU1NFOVlaRkJoYTBVeldXdGtWMkpYVWtWaU0yUlFUVEk1TUZsV1l6RmhNWEJaV25wYVVGWkhjekZVZWs1clkwWndTVlZ0T1ZCaGExWXpWRlZTUTJReVZrVmtSemxoVmpKNGRWbFZhRkpPYXpGVlVWaGtUbE5GU1RCVU0yeEtXakpKZVU1WGNHbFNNbmh4V1ZodmQyRlhSblJTYWtwYVYwVTFjVmt5TVhOa01sSkZZMGQwYVUxck5IaFpiR1JYWkZkU1JFNVhOV0ZYUmtwSFdXdGtWMlJHY0ZoT1ZFSlNZbTE0UzFkclRtNWliVTE2Vlc1c1lWWXdXakJVUm1STFlVZEtkRTVYZUdwaFYwNTNWRWMxVDAxSFZsaGxSM2hOWWxaS2QxbDZUa05qTVd4WllYcHNTMDFxVmpKWmJURldZbXM1TlZOVGRGRlJlbXh5V1Zab1drc3hRa2xVYlhCcVlsZDRNMXBGVGtOak1XeFlUbGMxYTFZd1duVlhiRkYzWVZaT2RGSnFTbHBXYXpWeFdUSXhjMlF5VWtSVFYyUnJVMGQ0TTFkc1VYZGhWMUpJVm1wU2ExRjZiSGhYVm1oaFlVZE5lVlJ1YkdoWFJVbDNVMWR2TUZNeFFrUlNXRkpOVlZjNWJsRXliRUphTWxKMFVtNXNTbEo2YkRGWmEyaHpWVWRLY21KSVVscFdNbEp6V1ROc1FrOVZiRWhYYldocFUwVTFjMVF6WkhaYU1FNXdVVmRrVFdWVWFHNVZhMlJYVFVad1dGUnFRa3BUUmtwMlYyeE9RMkZYVG5SUFZFNXFUV3hhTlZFeWJFSmFNbEowVW01c1NsSXllRFpWTVZaV1RWVnNSVTFIWkdGU2VteHhXa1pqZUdKSFNuVlZXRlphVmpOb2VsTlZUbHBpVld4SVZXNWFXazB4V2pCWGJHTXhUVVY0ZEZwSGVHdFNWbHA2VjJ4amVHSkhTblZWYTA1c1ZsZDRjbFF6YkVKYU1IZzFUMGRrVkZaV1ZtNVViRTVEWkcxT2NGRnRPV2hXTWxKMlYyeG9TbE13YkVSUmFrcGFWMFZzYmxsV2FFOVViVWw2WWpKa1VWVXdSbTlaVm1oUFUyeEtWVlpYWkV0aFZteHVWMnRqTldGdFVsaE5WM2hwWW14R01WZHFTbGROUmtwWVpVZDRhVll4V2pGYVJWWkxUbFpPV0ZWVVpFcFJNRVl5VkVoc1ExUnRTWHBqU0VKcFVqTm9iMVJFUW1GalIwNTBWbTB4YVUweVpFeFRWVVoyV2pCc1NGZHFSbWxpVlRSM1dWWmpOV1JWYkVoVWJXaHBZbFUxYzFsclZrOWtiVXAxVlcxNGJGTkdTazlYYkdNeFRWVjBTRlpZUWtwVFNFNU1VMVZPUWxvd2JFUlBTRnBLVWxkb2Mxa3lNVlphTWxaWVQxUkdTbEl3Tlc5WmJXeERZVVp3U0ZWWFpGcFdNVXB5V1Zab1UyTkhTWGxPVjJocFVUQktjVmxxU2xOaVJXeEpWVzA1V2xkR1JtNVpWbWhPV2pGd1dXRkhlRnBOTVZsM1YyeGtVbG95VVhsaFIzaHBZVlZKZDFsVlpGWmFNV3Q1VDFoV2ExSXhXVEJhUlU1RFpFWndXRTVVUmtSaFZVWnVVMVZPUW1ScmVEVlJia0pxWlZWS2NGbHJZelZoYlVWNVZtMTBUV0ZWU2toWmFrNUtXakpHV0U1WWNHdFNNRm94VjFSS1ZtTXdiRWxpU0ZwclZUQktjVmRXWXpCYU1sSlpWRzE0U2xOR1NuWlhiRTVEWWxkSmVXVklUbWxOTWxKM1dXMHhhbG94YTNsUFYzUmhWVEJKZDFsdWJFTmhNa1paVkc1a2FWSXdXVEZUVldSR1V6QnNSRkZYWkVwUmVtZ3lVMVZqZUdKSFRYcFViV2hoVFd4V2JscEZZelJhTWxKSVlVZDRTbE5HV2paWGJHaEtUbXRPY0ZGWFpFcFJNRVl5VkVoc1EyRkhTa2hXYm14clVUSmtjRlpYTVhOaWJVWkpWVmhTV2sxdWFIZFhWRXA2V2pGd1NHSkljRnBXTUhCNlYyeGtVbUZGYkhCaGVtUkVZVlZHVEZOVlRrSmFNR3hKVTIxNGExTkdXalZaYld4RFlsWnNXR1ZJY0dGV1NFNU1VMVZPUTA5VlRuQlJWWFJLVVRCR01sTXliRU5XVjBaSVlraHdTbEl4YjNoWmJURlBUVWRHV0U5WVZrcFNNbmcyVTFWa1lXTkhUblJXYlhSS1VqRlplVmRzYUV0T1ZXeEpWVzVDYVZZeFZtNVhWazVEVFZkTmVWWnViRXBTTURWNldWWmtUMk50VGpWUmFrSm9VakZXYmxreU1YTmliVVpKVlZka2FWWjZhM2haZWtwV1dqRnNkVlpxUW10U2Vtd3hVMVZvVTJSclRuQlJWMlJLVVRCR2JsbHFUa05pUjBwd1VXcENhRkl4Vm01WFZ6VkxaRzFSZWxSdGVHcGhWMUkyVTFWa1QyUnRTblZWYlhoc1UwWkdibGxzWkZka1YxSlVUa2RrVEdGVWFFeFRWVTVEWWxkU1dFNVhjR3RTTW5neVdXMXNRMlJ0U25KVWJscHBZbXhLYzFwVmFGTlViSEJZVGxSR1RGSXhWbmRUVldoNlV6QnNSRkZYWkVwUmVtZ3lVMVZXVTJKSFRraFdibFpoVWpKNE1WZHViRU5rYlVwd1VXcENhRkl4Vm01VFZ6QTFaRmRLU1dKR1FtbGhNbmd3VjFaa2EySkhUalZUVjJScllsVmFOVmxXWkVkaFYwcElWbGRrYTFJeWFITlRWV1JQWkcxS2RWVnRlR3hUUmtadVdXeGtWMlJYVWxSUmJrSnFaVlZLYzFsV2FGTmlNWEJaVTFWMFNsRXdSbTVUVlUwMFpHdHNTRk51VG1sTmF6VjVWMnhrVWxveGNIUlBXR3hLVTBaS2RsZHNUa05oYlVsNVRWaGthVkl4V1hkWGJFNURaREZzV0ZwSGVFcFNlbXcxVTFWak5XUlhTa2xoTW1SaFlsUnNOVk5WVWpSalIwcFlXWGwwU2xOR1NtOVhhazVPWkZWT2NGRlhaRXBSTUVwM1YyMXNRbUl3YkZoUFdGWnBVMGQ0VVZsdGRITmtSbXhZV2tkNGFtUXlPVzVUVlU1Q1dqQnNSRkZxYUcxUk1FWjJXVlpvVDFOc1NsVldWMlJMWVZac2JsZHNhR0ZpUjBwMVZWaFdhazB3Y0hGVmJHUTBZa2RLV0ZadVZtdFJlbFYzVjFaa2ExUXhiRmhOVjNoS1VrUkJOVk5WVGt0VGJGSldXVEpzVEZWWE9XNVRWVTVDV2pCc1JGRnFhRzFSTUVaMlZURm9UMVJ0U1hwaU1tUkxZVlpzYmxkc1RURk5SbXhaVTIwMVlWZEdSakZhUldSSFlteFNkRkp1VW1GVk1FVTFWVVpPUW1GV1RsWk5WV2hLWVZkMGQxTlZhSHBUTUd4RVVWZGtTbEV3Um01Wk1qRlhUVWRTV1ZOdVZrcFNNRFZ2V1cweFQySkhTa1pVYmxwcFlteEtjMXBWYUZOVWJIQllUbFJHVEZJeFZuZFVNMlIyV2pCc1JGRlhaRzFWVnpsdVUxVm5kMU13YkVKaU1tUktVako0ZEZOVlRtOWhNa2w1VkdwR2FWWXhXakZhUlUweFlteHdXVlZyV21sU01Wb3dWMnhqTVUxR1JuVmlSWEJoVVRKMGJscFlaSFphTUd4RVVWZGtUV1ZVYUc1V1Z6RlhZbTFHV1ZScVFtRlhSV3h1VjJ4b1lXSkhTblZWVjJSb1VqQmFNVmRyWkRSaVIwNXVZakprU2xFd1JtNVhhMk0xWVcxU1dFMVhlR2xpYkVZeFdXcEpNV0Z0U1hsT1ZFSmhWMGRuZDFsc1pGZGtWMUpVVVZSc1NsSjZiREZWVkVrMVpGZFNTRlpxVW10U1ZFWnpXVzAxVms0d1RuQlJWMlJ0VlZjNWJsRXlhM2RrUmtKdVlucG9UVTB3TlhGWk1qRnpaREpTUlU1RU1EMGlLU2twT3dvOEwzTmpjbWx3ZEQ0PQ=="

    # print(txt)
    # print(base64decode(txt))

    # print(base64decode(base64decode(txt)))

    txt2 = "UEdScGRpQnBaRDBpYzNKalgzZHlZWEJmUVRBek1qZ3pNamd5SWlCemRIbHNaVDBpWkdsemNHeGhlVHB1YjI1bElqNUVhWE5oWW14bElIbHZkWElnUVdSaWJHOWpheUJRYkhWbmFXNGdabTl5SUhkaGRHTm9JSFJvWlNCMmFXUmxiend2WkdsMlBqeGthWFlnYVdROUluTnlZMTkzY21Gd1h6QXpNamMwTXpreU15SStQR2xtY21GdFpTQnpjbU05SW1oMGRIQnpPaTh2YjNCbGJteHZZV1F1WTI4dlpXMWlaV1F2UmxSV2VHZFVjekJZTlRndklpQnpZM0p2Ykd4cGJtYzlJbTV2SWlCbWNtRnRaV0p2Y21SbGNqMGlNQ0lnZDJsa2RHZzlJall3TUNJZ2FHVnBaMmgwUFNJek5EQWlJR0ZzYkc5M1puVnNiSE5qY21WbGJqMGlkSEoxWlNJZ2QyVmlhMmwwWVd4c2IzZG1kV3hzYzJOeVpXVnVQU0owY25WbElpQnRiM3BoYkd4dmQyWjFiR3h6WTNKbFpXNDlJblJ5ZFdVaVBqd3ZhV1p5WVcxbFBqd3ZaR2wyUGdvS0Nnb0tDZ29LUENFdExTQlFiM0JCWkhNdWJtVjBJRkJ2Y0hWdVpHVnlJRU52WkdVZ1ptOXlJSGQzZHk1emRISmxZVzFrWldabGJtTmxMbU52YlNBdExUNEtQSE5qY21sd2RDQjBlWEJsUFNKMFpYaDBMMnBoZG1GelkzSnBjSFFpUGdvZ0lIWmhjaUJmY0c5d0lEMGdYM0J2Y0NCOGZDQmJYVHNLSUNCZmNHOXdMbkIxYzJnb1d5ZHphWFJsU1dRbkxDQXhNRFUxTkRJeVhTazdDaUFnWDNCdmNDNXdkWE5vS0ZzbmJXbHVRbWxrSnl3Z01DNHdNREF3TURCZEtUc0tJQ0JmY0c5d0xuQjFjMmdvV3lkd2IzQjFibVJsY25OUVpYSkpVQ2NzSURCZEtUc0tJQ0JmY0c5d0xuQjFjMmdvV3lka1pXeGhlVUpsZEhkbFpXNG5MQ0F3WFNrN0NpQWdYM0J2Y0M1d2RYTm9LRnNuWkdWbVlYVnNkQ2NzSUdaaGJITmxYU2s3Q2lBZ1gzQnZjQzV3ZFhOb0tGc25aR1ZtWVhWc2RGQmxja1JoZVNjc0lEQmRLVHNLSUNCZmNHOXdMbkIxYzJnb1d5ZDBiM0J0YjNOMFRHRjVaWEluTENCbVlXeHpaVjBwT3dvZ0lDaG1kVzVqZEdsdmJpZ3BJSHNLSUNBZ0lIWmhjaUJ3WVNBOUlHUnZZM1Z0Wlc1MExtTnlaV0YwWlVWc1pXMWxiblFvSjNOamNtbHdkQ2NwT3lCd1lTNTBlWEJsSUQwZ0ozUmxlSFF2YW1GMllYTmpjbWx3ZENjN0lIQmhMbUZ6ZVc1aklEMGdkSEoxWlRzS0lDQWdJSFpoY2lCeklEMGdaRzlqZFcxbGJuUXVaMlYwUld4bGJXVnVkSE5DZVZSaFowNWhiV1VvSjNOamNtbHdkQ2NwV3pCZE95QUtJQ0FnSUhCaExuTnlZeUE5SUNjdkwyTXhMbkJ2Y0dGa2N5NXVaWFF2Y0c5d0xtcHpKenNLSUNBZ0lIQmhMbTl1WlhKeWIzSWdQU0JtZFc1amRHbHZiaWdwSUhzS0lDQWdJQ0FnZG1GeUlITmhJRDBnWkc5amRXMWxiblF1WTNKbFlYUmxSV3hsYldWdWRDZ25jMk55YVhCMEp5azdJSE5oTG5SNWNHVWdQU0FuZEdWNGRDOXFZWFpoYzJOeWFYQjBKenNnYzJFdVlYTjVibU1nUFNCMGNuVmxPd29nSUNBZ0lDQnpZUzV6Y21NZ1BTQW5MeTlqTWk1d2IzQmhaSE11Ym1WMEwzQnZjQzVxY3ljN0NpQWdJQ0FnSUhNdWNHRnlaVzUwVG05a1pTNXBibk5sY25SQ1pXWnZjbVVvYzJFc0lITXBPd29nSUNBZ2ZUc0tJQ0FnSUhNdWNHRnlaVzUwVG05a1pTNXBibk5sY25SQ1pXWnZjbVVvY0dFc0lITXBPd29nSUgwcEtDazdDand2YzJOeWFYQjBQZ284SVMwdElGQnZjRUZrY3k1dVpYUWdVRzl3ZFc1a1pYSWdRMjlrWlNCRmJtUWdMUzArQ2dvZ0lEd2hMUzBnU0dsemRHRjBjeTVqYjIwZ0lGTlVRVkpVSUNBb1lYbHVZeWt0TFQ0S1BITmpjbWx3ZENCMGVYQmxQU0owWlhoMEwycGhkbUZ6WTNKcGNIUWlQblpoY2lCZlNHRnplVzVqUFNCZlNHRnplVzVqZkh3Z1cxMDdDbDlJWVhONWJtTXVjSFZ6YUNoYkowaHBjM1JoZEhNdWMzUmhjblFuTENBbk1Td3pNelF4TVRjMUxEUXNNQ3d3TERBc01EQXdNVEF3TURBblhTazdDbDlJWVhONWJtTXVjSFZ6YUNoYkowaHBjM1JoZEhNdVptRnphU2NzSUNjeEoxMHBPd3BmU0dGemVXNWpMbkIxYzJnb1d5ZElhWE4wWVhSekxuUnlZV05yWDJocGRITW5MQ0FuSjEwcE93b29ablZ1WTNScGIyNG9LU0I3Q25aaGNpQm9jeUE5SUdSdlkzVnRaVzUwTG1OeVpXRjBaVVZzWlcxbGJuUW9KM05qY21sd2RDY3BPeUJvY3k1MGVYQmxJRDBnSjNSbGVIUXZhbUYyWVhOamNtbHdkQ2M3SUdoekxtRnplVzVqSUQwZ2RISjFaVHNLYUhNdWMzSmpJRDBnS0Nkb2RIUndPaTh2Y3pFd0xtaHBjM1JoZEhNdVkyOXRMMnB6TVRWZllYTXVhbk1uS1RzS0tHUnZZM1Z0Wlc1MExtZGxkRVZzWlcxbGJuUnpRbmxVWVdkT1lXMWxLQ2RvWldGa0p5bGJNRjBnZkh3Z1pHOWpkVzFsYm5RdVoyVjBSV3hsYldWdWRITkNlVlJoWjA1aGJXVW9KMkp2WkhrbktWc3dYU2t1WVhCd1pXNWtRMmhwYkdRb2FITXBPd3A5S1NncE96d3ZjMk55YVhCMFBnbzhibTl6WTNKcGNIUStQR0VnYUhKbFpqMGlhSFIwY0RvdkwzZDNkeTVvYVhOMFlYUnpMbU52YlNJZ2RHRnlaMlYwUFNKZllteGhibXNpUGp4cGJXY2dJSE55WXowaWFIUjBjRG92TDNOemRHRjBhV014TG1ocGMzUmhkSE11WTI5dEx6QXVaMmxtUHpNek5ERXhOelVtTVRBeElpQmhiSFE5SW1OdmRXNTBaWElnYzNSaGRITWlJR0p2Y21SbGNqMGlNQ0krUEM5aFBqd3ZibTl6WTNKcGNIUStDandoTFMwZ1NHbHpkR0YwY3k1amIyMGdJRVZPUkNBZ0xTMCtDZ29LQ2dvOFpHbDJJSE4wZVd4bFBTSm1iMjUwTFhOcGVtVTZPWEI0T3lCd1lXUmthVzVuT2pBZ01uQjRPM0J2YzJsMGFXOXVPaUJtYVhobFpEdDBiM0E2TVRVN2NtbG5hSFE2TUR0NkxXbHVaR1Y0T2pFd01EQTdkR1Y0ZEMxaGJHbG5ianBqWlc1MFpYSTdZbUZqYTJkeWIzVnVaQzFqYjJ4dmNqb2pZalF3TVRBeE8yTnZiRzl5T2lObVptWTdiM0JoWTJsMGVUb3dMamc3SWo1UWNtOTBaV04wWldRZ2QybDBhQ0E4WVNCemRIbHNaVDBpWTI5c2IzSTZJMlptWmlJZ2FISmxaajBpYUhSMGNEb3ZMM2QzZHk1emRISmxZVzFrWldabGJtTmxMbU52YlM5cGJtUmxlQzV3YUhBaUlIUmhjbWRsZEQwaVgySnNZVzVySWlCMGFYUnNaVDBpSWo1VGRISmxZVzBnUkdWbVpXNWpaVHd2WVQ0OEwyUnBkajRLQ2p4a2FYWWdhV1E5SW5OMGNtVmhiUzFpWVc1dVpYSWlJSE4wZVd4bFBTSndiM05wZEdsdmJqb2dabWw0WldRN2RHOXdPakE3YkdWbWREb3dPM290YVc1a1pYZzZPVGs1TzNkcFpIUm9PakV3TURCd2VEdG9aV2xuYUhRNk1UQXdNSEI0T3lJZ2IyNWpiR2xqYXowaWFtRjJZWE5qY21sd2REcGtiMk4xYldWdWRDNW5aWFJGYkdWdFpXNTBRbmxKWkNnbmMzUnlaV0Z0TFdKaGJtNWxjaWNwTG5OMGVXeGxMbVJwYzNCc1lYazlKMjV2Ym1Vbk95SStQQzlrYVhZK1BITmpjbWx3ZENCc1lXNW5kV0ZuWlQwaVNtRjJZVk5qY21sd2RDSWdkSGx3WlQwaWRHVjRkQzlxWVhaaGMyTnlhWEIwSWo0S1BDRXRMUW9nQ2lBZ2RtRnlJRzl1YkhsUGJrbHRZV2RsY3lBOUlHWmhiSE5sT3dvZ0NpQWdMeThnUkdWMFpXTjBJSFJvWlNCaWNtOTNjMlZ5Q2lBZ2RtRnlJR2x6U1VVMUlEMGdaRzlqZFcxbGJuUXVZV3hzSUNZbUlHUnZZM1Z0Wlc1MExtZGxkRVZzWlcxbGJuUkNlVWxrT3lBZ0x5OGdTVVVnTlNCdmNpQm9hV2RvWlhJS0lDQjJZWElnYVhOTmIzb2dQU0FoYVhOSlJUVWdKaVlnWkc5amRXMWxiblF1WjJWMFJXeGxiV1Z1ZEVKNVNXUTdJQ0F2THlCTmIzcHBiR3hoTDBacGNtVm1iM2dLSUFvZ0lHWjFibU4wYVc5dUlHTmhibU5sYkVOdmJuUmxlSFJOWlc1MUtHVXBJSHNLSUNBZ0lDOHZJRWhsY21VZ2VXOTFJR05oYmlCaFpHUWdZV1JrYVhScGIyNWhiQ0JqYjJSbElIUm9ZWFFnYVhNZ1pYaGxZM1YwWldRZ2QyaGxiaUIwYUdVZ1kyOXVkR1Y0ZENCdFpXNTFDaUFnSUNBdkx5QnBjeUJpYkc5amEyVmtMaUJHYjNJZ2FXNXpkR0Z1WTJVc0lIbHZkU0JqWVc0Z2RYTmxJSFJvWlNCbWIyeHNiM2RwYm1jZ1kyOWtaU0IwYnlCa2FYTndiR0Y1SUdFS0lDQWdJQzh2SUcxbGMzTmhaMlVnZEc4Z2RHaGxJSFZ6WlhJNkNpQWdJQ0F2THlCaGJHVnlkQ2dpVW1sbmFIUXRZMnhwWTJzZ1pHbHpZV0pzWldRaElpazdDaUFLSUNBZ0lISmxkSFZ5YmlCbVlXeHpaVHNLSUNCOUNpQUtJQ0F2S2lCVWFHbHpJR1oxYm1OMGFXOXVJR2x6SUdacGNtVmtJR1YyWlhKNUlIUnBiV1VnWVNCMWMyVnlJR05zYVdOcmN5QjBhR1VnY21sbmFIUWdiVzkxYzJVZ1luVjBkRzl1SUhSdkNpQWdJQ0FnYjNCbGJpQjBhR1VnWW5KdmQzTmxjaWR6SUdOdmJuUmxlSFFnYldWdWRTNGdLaThLSUNCbWRXNWpkR2x2YmlCdmJrTnZiblJsZUhSTlpXNTFLR1VwSUhzS0lDQWdJQzh2SUVSbGNHVnVaR2x1WnlCdmJpQjBhR1VnSW05dWJIbFBia2x0WVdkbGN5SWdkbUZ5YVdGaWJHVWdkR2hsSUdOdmJuUmxlSFFnYldWdWRTQnBjeUJsYVhSb1pYSUtJQ0FnSUM4dklHSnNiMk5yWldRZ1ptOXlJSFJvWlNCamIyMXdiR1YwWlNCd1lXZGxJRzl5SUc5dWJIa2dabTl5SUR4cGJXYytJSFJoWjNNdUNpQWdJQ0JwWmlBb0lXOXViSGxQYmtsdFlXZGxjd29nSUNBZ0lDQjhmQ0FvYVhOSlJUVWdKaVlnWlhabGJuUXVjM0pqUld4bGJXVnVkQzUwWVdkT1lXMWxJRDA5SUNKSlRVY2lLUW9nSUNBZ0lDQjhmQ0FvU1hOTmIzb2dKaVlnWlM1MFlYSm5aWFF1ZEdGblRtRnRaU0E5UFNBaVNVMUhJaWtwSUhzS0lDQWdJQ0FnY21WMGRYSnVJR05oYm1ObGJFTnZiblJsZUhSTlpXNTFLR1VwT3dvZ0lDQWdmUW9nSUgwS0lBb2dJR2xtSUNoa2IyTjFiV1Z1ZEM1blpYUkZiR1Z0Wlc1MFFubEpaQ2tnZXdvZ0lDQWdMeThnVW1WbmFYTjBaWElnWlhabGJuUWdhR0Z1Wkd4bGNnb2dJQ0FnWkc5amRXMWxiblF1YjI1amIyNTBaWGgwYldWdWRTQTlJRzl1UTI5dWRHVjRkRTFsYm5VN0NpQWdmUW9nQ2kwdFBnbzhMM05qY21sd2REND0="
    # print(base64decode(base64decode(txt2)))


    import base64

    bs=base64.b64decode(base64.b64decode(txt))
    print(bs.decode())