import marshal,zlib,base64
exec(zlib.decompress(base64.b64decode("eJztfety20iy5m/pKTBwtEiNKEokdbHUh/aRZbmt07bkkOTu7VArGCABkrAIgg2AluXp2ejYndjoHxuxM7Ezc05MzO5z7O7j+Ek2sy5AFW4EQFKy1WQ3LRAoZFVlVWZ9lZVZ9eh3G2PX2Wibw43Rrde3h/XlR0rH1s1hrzn2uuuPl5dNa2Q7nmK7FffWrXimZVR0zTPIhaMNdduq9DW3PzDbFceoeH3H0PD1yjvXHlZ6hjfSXLcydgaYoGPb16YBV8tdx7YUazzwzJFjdwzXhVeqI9seKCy/C0LoDdxZ9pzb/eUldt8yOn1taH40lo0PHWPkKcfk/pHj2A6kst0qFNMzrLI6Mkd1xRy6njYYBK+pqzI9x/hpbLiem48cfwuokZrw31VKxbSHLq/IoT0cGh28RYiymvPi8FTPHPvGNZzl5Ufr54bnATfWHy0/Yp9lxxjYml6Goqwuwz9V1/B0o6sB+4whba1yCZrrcWl1ue0ozYB8ldEt4wN8rQX39YHRcuy27bnlF9rANSLPjK5juP1yQKXV97xR9eXFxZsz+uwNbTQbCFcs7UMLe0OzRghput6HljMcFwpyWS69hezXD3rG0CtVlNLpyHC0jb3q402lfDDUHdvUv1bITeW1OTQ3GjvVerVe397aqNX2qrVG/Wvl7deKqa8qbyBfz96oV2v16la9oXwHOQBTN+Bnbae0eoWsMz6YHvANeKPgZXlVasJSZ2BoDvBoaeSYQ09Rf9xsNC5rX+/VrMvfXSmHAxt7oeL1DcWDfletVlXpdXdgGCOloaysKD4l4fEHvbduj4yhgsxy9zc2box2tat1jDb0+mrHtjasa910BvZ7o9ozveDtKi3rssI+mHnL0sxhqzsekp4DD6F2B0PT0vAnqyIhV/4IleRvdm1HgS41VD4qa0rpx2EpeMQ/pPt4uj32qjeO6RllYzUtTXcwhp4QTYINXiUMKW/ip1rDIuJHeXX6zalC++3A7tnQC1RVXQ54/emv//3TX3/5Mv//c1CN5U9//S/AiE9//1Po/zCr6OfT33+dcBvoxVD/1U8okE/8AekzJ6R3UnIO1+vT33/hb5KnvygK+4f/CJ7AN9tPWqpfJnOApuP//yo9+VV48ktQuV9TLjmVDPn+wlnA8/1FYM4vsTd+5Td+DadIvMEpJ7ZI8Q+8DzT+et/CU/j//xB44SuSuhUoJdaev/xXBb7kx1/wX/6bNZ34PPR7Qkoxpz+lU4r7/aeYnBJS0pyCWu5an/72109/+/OX+f+/S/X4C//RsH6vBA8uDM3CSgeNvO9f78BTxxp/ABRlWYBOXOG9yd3+b3/Jkv+ZARDKSMr/HECWNlTO+5pjak75W0AIqxkLkTH/b0yvP24n5c/BRI+kIjDC7WsfNV1rubRMGy+evdQ619EyZcz/whgYPUez4vKv07tbfjG8qmVs4I8LxwDg12HNQlJtWml8yViaQ8fQTc9N4MYl8v9KuTx/++ri4AQvXh6cHR+cXU1ukoz5n9ie2TGE7BWpN/ZNVznvOCbMFA41x/AMXWnfKrQ4ZVaY1WpcaTLmz2BtbP391qgBSN5kPE/qfekMCZfmH/etKgr//78QXcKsFWdICgXGZLKE2N8zyV2Yh5SqUOlSpVStsj9VpXS1vISA2UbATFPCK3RuUFZ/dITZwad//x9XQiu8sskUV2CxumavVr6O4uavBZyMCLkNggrF2Vym82QyRbpadsc4meqOB/Rnp290rkc2TlHIb/uapdPIZKDV1cyBodNbpt51TGPIKeFP25JuWYbVNpyWyV4AqTUH5Go4xgf8Pf5USNVCWi2JWH/E/0bygfqQ4sm/eo49Zu+grjB4ncj9lnRrYLqekPz9eDC08RGdpjVqKJrKd3BXJc+CJ3WL3mXzj07fBgl2lVd2DxqWTkSwV8RNq1Lnhzh7icwVieiurwed44nQMWpVQepObMfSBkjFhMLlolMX6VzY18bQLUCnZm2KdI5glpnwPtwm5FuW4fVt7AuOdtMyh6MxSkJITQhZPXkiygAwzuwqMqGmqvpCFZpvf+9A91BIJpD/EpsELxmDGCI1QoXcTUxTJ2m6bQ/5lZhqk6QKMnONfOULJrnHJ6xzPWqGPlwLkdImdDFqhILitkh5geVoOyiXyFtV74MHWookXAIJGZOyUgNV+VvjlliSKsen5C/mEJuF1I2ZXiuJWu0//puo1V4cHB49Oz39ltUtlJAQNOWuIRJb80k1dqzj50G3+DkYPY9Qqwg9UhjjgmIotOg3mBUzH1bZ3+QM38DTG9vR00jSUQEuGOuX2k6V8pyDG0sy15CXGNMDU9jbs1fcOOh3m6HccU5speMb/bDr+N0NswT13fFs57Zquq2+Z6HOv3DGBn3oAhbreC0Ylqzy0Glusnfw92WJKOXSFbxg6uJ9ZA25DUxjZMZti+U4djAHuAc8hGtyD8Si5GrvjXXdeA+qsoQDIDwjVeLMWXLNXlMpaSOzdW3cNh8/rmuPt/Y2Gzs1Xdt7vLtZb3f3drXNek3XO7UtvQOwDTS5qQ3clnc7Mpoj1iJ0vCmtmfpaCYurec1/Oz896RlDw9E8AxRyp28ODRifmjX/posGYRjpqL3YbdYGdkcbGE1j2Hp7TmW5qY29fpVIC88KcgEOrJUcrOmw5bqDlmO49tiB0aC5+b5Zq27u1LuPO8Zed3erXYPLrU6t3uh06o2txq62pTXqJVJ1XfM0YNofVFZ7dV+dVH+1ooZZAG/xksFTwgd139QrKmUDPEZGqBVFjWEGPK3BW0kcYY8pW+AHYQzcoLyBGwF34K5fjH3gT0WN4w+8sgkp3yPh6qb6R8KHD01m2a8OjZuyaunbqOPxQXU8wkWAMnQSekdrfqj2jQ+62TNc2vEoG3nCP5QgaWlf+yN9RHulygUP+CxbStHW6xrOe8OpjvojIkNLTtO3skNfLgOJykiDeYvbxIwo3Y9NXHaooqi7ZafqGR88+mBkEuBF5F31dSwwv3RTClIwk+jHy5LWQUhGdXPpSkjRGdiuwSpI9WtJkv9A23365/8M7svwEYEJgD6G+ga3pYh9Nfzxqz6ygb++xoJ526gfMjIbGwyXPWWSgq+sjE3dbfZuTGvsao0VsXogNgkV5iOPrwZjljmqofWN/YAzGRRjoBlRJwXAV1JJHJGHqAXzp4NOxx5DSxz679N+KgyKjqWsO2xMJqMrSSCjc7E4HBgkZU7b8AVB4vkz26xu0vw4omGo4uL026MTAbL6YCYDThWQRAx4g1I/FfsgAZWxk1wK5NgwYHs3SE+Uu/S+9zTUs3ipsLaoUwXxBNq+gEKyoWYZkEC7LOEVTs4mCq0gsmI+ITkN4ScOn3zYF14HIriPIL5srPxeAxqerZDSwuyFlONpwM7L243h1b6isl5u+KBY7G38wS194iPdoCPK+PP10clb5VHmD10vIozIhkebsWi0ipNWgZcMgaYD0BB7Sc9TcGrXBaHV1eXJohMjOT6DPouOSnAx3DB1/BnT0TJzJ1WpTcmqfEo8rnQRBc57sLBODkO3QfRvzCRasHqlDJXiHBp5HW8KU9dYW6wJM1S1eFbHz5V4GyxmhYA7ZuL8D3Vta/P3kNefc07wJUMBrpDDeEdhIWVsYWPBNwZIpb5B0OYGQU55SDVEUmhUVrjUKBrrjvInJ/0tkf4z2ytGZVukcur10dWgcJF2RGLnffuG6m+JIL/KQ3dXamECgosX8rFI7DnMEYGY5wA2L0xxT6QIYOZ0LDXttHYm4kQxcmxcV3DjyFKjEzPVgQZ5tE6GKP8GaCA2+he3RFECogUqdqgPTDxBceiIzAlQ65MgoZEU1Pakj61R5FGDPMKxt9UHiYo83wqet20v8nibWrXGw07k0Y6azfKTcUyPYdGaiHN+gJkiFQ4RNwoNr/qDKBATm03EzkIzPUMFIyhjVUBrvMdIFd5Vo/4sMdUPJxGYEf9oa1P5vVIKCvbjB6P+44e9bfhuRqdmQo496OkjmMAptmPifMDS4H5cEUSbWUZuxFDxkazIlMe8FziGZb83yiV7TKCAlGgv3FViwUOqM9PNTWiKbn78WLW0HvxhljIz2ntTrK2ZZZEh3uOTF6fC1EiSxjlh2juAr5NmdVomkytI59EQep4iGl43gocIoxIme5ghdSSTTMP//H/yFAc6uqZY5nDsGcLL1WoV33fyQW/fPpEMwaHlbmUQ7htzcMnOJEt2kOayhLaf0tU+nVsht+CJyaE5yKVwD9E5mUp9CJdXTSkvgD/66poqF1iV5gxLH+XyfgiMT0zJ1H8vDWB/ViVzK7clCW3wv/+v2AZiG4pruvsKsd/4c5HI9EOJkn6ajXDwxgnv76V8hRb7o6jJWKHpfCl/kZPJTl/k8CJFqMjMCF+k1MmUpy81OnGM+vYw3JKs1JbdNgdGi6QoVvjkDKYv/Cu7QxR5mDes8AP2uHQ1TTdPzmT6CjxHdG93lbbpeH0hA1YBclvXbosVPJn49AU/h2HWjumTUHBCAJXtT8ShGHq+PubtQKkH+cTkFMYu8PnP4rCz9tNlySW5y82ahT+ptMPMiJLTXBcfFEWogVk8MBITkomLyZ/++fcrOsuXcMOUEJnhoudvX78RcBGdgzxcQFTYykIsI88Vij2mNrFwQgoJ5yhEtBEmSp1fqL8O5DCNbSVCji4/TmFniVAkg4FCnYimsbkgYVK6YlzcTaM1Res8DtPVGJ2SO03V9zKSLVzykDEGFUiM1cV2jRazVjxaxw+bbnEjTPB8309PSjSNPUaik88sI5SXTjBDtKiFhs0rWqaelI7aaUxdcm1LStzgiZkLHen+SYmpGcewMiWmRp2hnSnxDqMM3TopyW6QJFPNqM2A9LcW7W9JKfciKTNlsOkbtQrM+4XG5nN/rm5dcXFUaO0vd7zj61dulc3CufmGFub0PCgMARlB+glWv5C7RNoUN2lKLs9wE3wrJhoPiJYb+CrZ1AXNwAwIaVNkS7s2Wr5rKW1B4NFG0PysKemaMCJWjSHWwDaw5PvJVrURkNDLbLWOArogC7aczJ6yKDphFi86Bu8KUA0XiVzPKQ+geH5eq6vi2pQirDY1JfW4xgszyYUYes8m7T9ikYOlbo6URd9lfpnikHIuuKKgz12kjaqlQBhE2muyS4GnDVBUgwSioekrV/0qzB60meOYJ48qiTmca+8NpQsTWeXG9PrKMGTVElitrnKbKCZK6DB4s7SGBfB5l5b7C8wY3eb0hBoiPdWnVxTd+8NcJm1EHiodUGEYM0yYM83UIpQ5+pq2bc3Rj9G66IxHXuXo9EXgdcp5JhXp3LNBxKhXzIzKEfHZkPQNZ0NphjkWXSQnU72kZfJgNHtxdvoa/jk+Onl+Lhq1w8BkMa5FxjVT9xL9ciR5PcbHwkwtXmhJ43NDhgtilNM2rHsT7ML2SDYMYx4h27BYhQzq+gV0kSS9t2aPLlXUeerVctT2EZsjtP0LyiGp8YvbR7go5YEgnJNd0xjobpMP1gMT/Zi3McJ8deVOsIkw75o1TpFkOxG0sOdoFQvhFz/g5o4wjJ/fAsck4RiBRfeEZeI61QLYLIDNfQKbb85O375RXh+9fnZ0JqMb2d6x/1tHMs0MC/s+jKHWV0FCBR1RElFMaNhNW4wnNDeemjqL0AkHBkhIRnNvEsIriqKY1DrBcOLeCEtDWcHMN4TmrLFMJighGchnZegQZUZCDY6RvaFp8zJaLodZyNuKqa8QmNXcEz5pHcGVeoER+EZzFONK0MUPQL4D2OLntYAscZBFYM+dwpWYLrzAKAuMch8Y5ej1wfErClOotg7wSWTxZoFPFvjk4eITulA+E4gSkpy7QSkzhCg5HUK1KR1Cfb8pw4KqclgUOBeSRDHQKEghoqMc8IjklxkaBdmtqcrPihq4mQKBoZoDMsXKBlNHqXgqthfOCmpxTxGyHysRCVnc8+KvI0mgEiAYa4I7hV/x4rlAYAsEdh8I7M3L05Mj5eQtsQ4J9qIAiEUcYxZAbAHEHi4Qk/z+ZoLHQgK0wGMZ8RhtAwGQyXETKbhMTlgQntHs8+AzOduHCdOibrEzQWsnsrwlwDXeJHeK1+LFd4HXFnjt/ixmopmMeCL/xjHZ7GNew9vOFHdjmallh/qUx/uskDhcbZqhe9rYWsGUcqd2lIURRTKizNlkcuf2kminX4y+i9H3nterov7CcRE/C5fhGPvJwmX4S3EZzgOrSoSXpXvAVjP3EjZ8CU73Ev6sEFdY+dwpAgtnvkBkd4nIoty/Y4SWJi4LrLbAave+shWgNDnOeoHPIvgs7xjMbMHUMJxr+B07A2Hb+UKh0BSkhLeix3yTgpASF2ksEk0fP9APaTiQigO9WmigH85qoO+P7m1FpD9arIbIo3vcMuHMVz2Q7Xc6nsfJwmIUX4zi9z6KJxheUjZEWYzvC/vLwv4yN/tLdHusmbnMfGkGGOkQxnuEaEUixRdobZZo7f4C0dPFZgHhFhDuPiAcOR3p5cHhtwJkE05g+HIh2tx2R31tDk164ssLNlqVBWWkOaDMgtSr02yf+no88EzlmTP2DBhPO4af4TTbp56PR6AnZ0VaPqYGyb1AcjPkiLS16g9a37bpOU859xPNvtknO3rkUcJen75c9LUpD11BAgU295SORqGF4Lt6WtA1I4/oRp4dh722xE5TjKSje3i62D0iz+iWnW1s38iz7eBUlltsnkiCqXe4ZDXmGuv45Fh5+ULUV6TavyFVdRkUB8/6CB5cCf39om8oHhE+/0Qqa+x6Stvg+4H+yM9uInDmFg+t4Sm7puN6v/MlJA75McaaCWdgR2AaLYoceR+GTNMerxGdlE2a4KbPLRLnYhz1CgVNPYMCt7cXj8GLVlRiFtFwMdUTelE9nl8SmVM8lmYUPvA5mVwazP9Yowf3kZ7RYjOPUq3eQIzOjgEeOwM8Ahf+0IMoOe/b65Fja+mBqxvB4btyM9Qbu7vbe3ube9t7tZ3t7a/q2/Xt3cPNbm1rU9Paht5t72xrnfquttvYM/SaVq/vNNq1FXZsMjbZiqtft94bDp4F3Kyv0MOV1bWyqcPEa0U8JXnFPxUZHkM98Tm83DRtdyX5nOUVPPW50d3e3u7u7UFxat2Ovqtpm52tre724+52vW50d0inlo5nKfMTePEUV+kkWZwt3wZGjOTTpV74Roxowgwzr5hDTPYVVeqdMYRD3Ru36B+Guzg9/C/D2/wM8tDbwPupTDPSyWHBkQPI6fCZTJTbl6qBar5luT22cJSd9/EDGP+VdCjlHNtsykabttWKN1uo3YKGA6VTjyodNL6A2tnalk4gfxCqpz5r1ZOkfFLVTx4hmGN3nrY/T9Gh65RA8R4d7tJCn86njnK1RVGVNNdWnLoZp2/HaRoy0pJiU4KCalAFNdDC+qnEkjwk/dSYvX5K1lATdFQ+yZhrD5++i0/RxxucxDSdPNrLpW6eV2flbJviemvO7TqDhp1Fy07XtDFtKzfukmXr7Jh2+fg1puK24BkmqTrGaAAdoFzaKFWUUinI4SHpuK156Lg0LTdRz+WVpjnLxCyEYgqp2AqITCcWcXIREoz8ei93W02j++be0jNp6tm09bSNHdva4eZeGmh9mGkm6sKlpXcaCjJNlqwPUWtux5jL4G0hzUPSmtvz0ZrpejOD5swvj3OXqdkI1RRStS2SmVas4uUqIlhFNGmBtptOm95B28+o8WfV+tM3f0L7RzsAqMQdkGW1DQXXhj2YIcusf0jacGde2nCSPsykEYvI1R1IxqxEYwrZ2JEJTS8cSdIRIx7FNGShtpxWS95Jb5hZd5hdf5hFh0jsEXFdAnTmLupMV7ulKrOi0MuKwtQoXGjvzGFPG8Ij2zLsoVFRtCHeqiij8bVpaddwMdBu2/ZtRdFtRzMse4iv9bWeqYUb9iFp4d35aeHJejijJi4mv3cif7MTwCkkcDdMahYimCyDsUJYVDMXbNvptfMd9Y8ZdpAZ6ugZdZGUPhLfSeKb7dx2HNC76HOreDYJolC8wDHL983ZL2fsB55zq6AL1NAGMo5yo91Wo2/OgQNJzs/h8l0YpGKSb1zR4ogF8L3/AsdVhbiaMj9A+vTwjHsyU5dNhztr9gZ2Wxsopj4wXa9C2F5B//QvxWcwn8Mgrabkl5foI0YiCY6fKwlxBIQ0sisbtTdhZ7MoNc5czJeFFZVpgVcriupk8wM8BwHyYjzaMO7oA6pmB8CRUd7aXKUeVSbx1fX62GaAjaoX5KpMxbDpQkcBmAQ/3GZ5dZW/UXUxFyr/9FU/dggf8/wIcXPIqLt+htV3Nm2uhA6ihIMVSFMEPWSaCAJJdFAUSBVFUXDHLP6m0vEHkgoN/Gl1AWIZeqUN71fGo+LhjsCqlunxVmbCx9t4PGIPIAmTpao7GpiU4Td9ZAZ2EsLPMRtJ4BW8R9IPzKGB73iOSSPycM8CRdi04HNCq7wC6ZgVr2eJWpEp8ZCebcSwZI3cfjyUBdTTph7cComdGo9WqTAttYH71yxJFOIiRZbOdDXe+Co53KrdbUFDgH5ToRvcsDEHk7FIO86lNfVnGNuRGzS4LUgXxKTljiYMiIddfrHIl3JNWDBgcmzhki9AXCeIDtqiE+63AuLCSD9FLMrPqsIrqjSfCFF9zBUuEXuSMkfhJxFmQeh8vndGYb7zpFl476cV+R8ojlQWNKzDN5/++Y/JLAh5/0nKiOfgyxHtEthB15rEAVEIf6QVSo5J/D/xAPgQ4QLCXmHwEkpdIoGcmOXqWkkJ6D2JpOHiAsmaTwL6r8z3RgzpHSt4y+9Uq2IeGBMqcBPZPoFO0DSrq6sxkaEpqGUoD0rniD/U5bgIhjmEp9Gxikeo7DNYkxaGAFjPZ9oyGY/bZJd8fi8I02uvktSHL48Ov6UpO5gyYFWQtEOTSj0wrRDSeN6Aun2A0Zy8JbTh+voTBbq6wttIor66ShgqhOYFH+X87ZujM+X1Mxb0InwYv0ZsuyQ2tgcb8HwZ6Bb603QBMVlj96iEk3AXgpBpIMw0MXqUohBjP01snkBM3LhfXWZxOkrh0DyB8gsaljvr0DmMk2vx6DEeMCfeRGEG3DBVyBwlkC9mTioYHVE5GRo1N/tdt2LPs80VmjR5cy0kGUInjnRYiEu3xRK3XwgOlnX9g2UlhtQzMmSxTcnnvk2J3+Gzd17otel7heQOroNmmbobm2nd2Izvxo3M3bj3mR0X1VucFzVtV558snjec516eY4DL3y40yh6uFPQ0Ue8o3MkIPZ3hcRnK6FPTPcPJxGEIfyI9OTwTf6ZrX0xKRdkCtp4kC+iAcmHp/iQzBKSKATl5XzEV7jFKJpzpHsnEYyG/0bMd6XEl0WmZRSEFC7FI5sg5l7YLyBX4L2M5+SKJwd5p5+uHmyFRM5V50SLWns9EwUJuuFlqQpkYOJSrbI/VQX1FfYgm5hmSUpxl5hCpgGxJvbEHZdqfNYS4l7MBHKZTDdhpkdWLNiSxhLZ20CDKZHm9IjpjU3vBIOtfY2bNqFRBN1NnZ4wBkWstTHmWr7rE3/nEdrviTVFy7e7GZYAtGTavmZLbXmY14SxC3OFp+2E8PIvyS0BOTHRyDvzGPOlnxKNuFEL7U/7Rc2nUZj9U267aWifJtlYGm8qDWyEtVgz6RKIgWggpElD5sRES+pPcav4sXZU+IKC5HZUja+ZxhhSfSNqTTCixltRY8yooTqIC85EQllcI6aoJ4gND49+cKIzhxjpJOFJF5/5ClCqCE0pRPV4IYoXozp7KDo95BOlfMKULk51UZySBCpVpHh9ZC8OIlZ+wB2ma1DBSg7sfXCSNZfo3mTZmiRd85avCRI2pYw1kmQsXsoa/mPZuSivpOWVtXRpa8jSlixvqRIX1C3sOUWkTgjyYoGo7fjgK6Q1ORb1wYnlnAJS0wRzsmjOXzgniueUArqVLKDxIrolJAh7AOYX0/yCmi6qW2FRTRPWVHEV6xl1dSQiK8UQ4Tvbkpe6WmHX1+NwmM9DE865xT2mi2cWAb0LEc0gpFOK6XaamMYL6raUJOqsW0RYi4hrusBuRwU2XWRThVauc5yHMhHckLM0vhkOyqsIP7a2Q77FD0185xioN0mAs4nw3QhxJjGeUpB30gU5XpR3QoniPO+LiXMxgU4X6Z04kZ4k1KliHa5/fOgBEe1IpMwcLLjiJ9maK36wEiSEjWiTnd3He5ugYbgYUn1jmcCBwcBA2EBD2OAK/jcH9nvj1h7jC9DzsFh4SWPZIkEPD001zTV6bbJyyqqe7kpBZVRRUyqp3UlKKl5N7UaSxYcIFVVVRZVVurrajVdXkxVWqsraTV6qvKsPZf59l4J/iHZ+/NkUR5n1uHDf9fE/CSPSfRfL/6B0PMax8J02HGvOLQxmXaPtsEtLczp9+KuBAhuQ33j33ZiMhu/GA/yljXtj18Nx0hh5xCEFrocwSrJL3ejQy8+n0ncyLN/x0Px4tkPzfTeR/4kDBfddJv+TBEfuu1yRz7zw0H3XK/JJAGT3XazIZypE+DiKCO+7PpFPHCR9/BmV8/PCY/4nMxq/74ImfjLOCu67mImftNnJYzY7ue8yJn4is6T7LlDiJ2W2BmrCdwwMHAKXlzBegsbIv7HtQbmB8VmjqqWNyuiQWFFMfXVyPFwpwccywRv9eeSMejz/MeJeHuNwevrtxuGbWJ9T8fhNUJPyoZsbQUylGhs5uRxzqKB8Ts8bJdNJjIJMAtGCnvDcGTccA5jtwzfQeHb29uJIeXF6dngkHKHFjvb6okMI8+2RwapAkH/GWKbnMV2nbh0hhdgnL0dCi7LzrxLiLEhoSmSbjcSifA+zEeKCH9AA7FXGW8ic1dQ4KyIybMSgO6GwHRn4E/JX9LDnLZZyAmzOyJN0bqyRVlmO81WPSn+QmxJIMakCSnvM3iTkbOOiG4y42lA3Y7lHYjhuSBAHpiHa1D+AeIQNO7rx3VZwbKuozPgWiVyf0j097HQ/uonk44eBL/mW8/g5y+dkNycX6bPzme6eQdkT3iHDJTNjwfo8YRcM4O9ICyAa2boovBUDTcNan1STHfI8EjdhYKkkqyyXkGGSjEQP64kV4qWI5Tx5O690sV3NSC1uqyCJGu+2PCye2tXzboix1DGuXZn7Ah4KtwMmntgMJNFcW6HA7m9fQOvl2y8iHiUECek5y7T2iXtTFNlzCas1cLHMiIz8X0Djpn+bOD4/lfWxAXqHvovD9FPh2eXtxvAqgWurJMqdZDMxyF2Vikolg715S17luYef/pD6dBgXORY8PikSWCYXlQHRHw5enp4qZDeOozO+i9t6/o9wZjU7f/Y3hGIL74Tx/Sz3wBjgzG1We2AExOQ9MHKRlDa/eOsKx9HPet8LPKCYn3ucdGa00C/trPtfPA/hdhBBfDmTWggViwowfZtueUGesMj8UIK6mMC24hM1gkS0kULPt4Lnko6hTwsFp8bUiymSV8fnF8qLs+Ojk+fCjFau4gNSCXk345ukQhi+vbxaXnrXcXERdXM5U6S9h1JF589JW0Yw/udZcU7a+URyRbJMr9O/lVE5e4sDczTJcNiHLNp4DQX9bjzg7XiD5Ss6DUyGcDgLJJNAWkQxnJ9wl25Whjzntji8jQ1MDtK+oXH+tAuyDQ/FDRhgQn4dYed0Z1yHlnFIDv7shk9gmZXk42WJNDgNyyAiRgqDWY1Av5ad0r9Wf0+jMWwP57wkTdU1cHW7TABmlehziggRzNMUHMXDW3yTwaq8VEwlxE+90bGHXbNHbz+tuk6n2R11vA8rVWiaQdPUV6oDbdiDi/Xj5ytVHUaVJidl6gEdvrmgU20B4zzbua2abqvvWVjfC2ds8MeuMQDg2cJ5annoNDf5e5cq35NOvcLoFGq5AGU1oJuO4qvjtoUg2FccS8I2NwLvVAsaSesZbvXo7Oz0rHV88t3Bq+PnMMs9Ojs5eH2kPuHMDSwLZKtR7BJkTxvGaJK3xGnRxgtls4cgvaxu2AiTcyatQ/JiNFDA2FSJ9I41pfTjkAfipK65fff21Ul43U0w2CprbOYVJMAVOCYQLIPI7ot88hK7RQlRhJ+NuTrJThOzCeAkgvHWZ4GzYc2nUs0YTF8LGqNFvM0H4sNXpydHMBKfvk4cjgVAsRiS8w3Jc9hzi5V7DjtupW64Ndf9tpI2Ks+w29ZUmy37YDs3dErZcqsAfiqRxinNCURRti2g1AJKLaDUAkr99qBUVP/NE1BRE+nro9fPfAupj6W43WUBo/LCqJlu+cjKXHjDx/T9HhO3e7yL3R4zIqmYvR7vD0jJ1ZsWR2Xe9zGlDYugLFKLGYIs7gi2wFoLrLXAWgus9WVgrYgWnD/UenH86igMtOgC1gJmJcIsXFh1s5mmSLuPNK8/2SgluSmSLLijHVPqMV6K2dgZcvmYHV4ptJCWYBaJWl6g1HGQIFk9MD6FGChzLHBaxNT7AXfjfRUnYIHUkTXDwJo8rt7tsJo+qiYNqoljavqQOt2IygdUH+JlGlaFUdUPEhDG1mJDa9rIOv3AyuBHwvj5mx0kw2phPmOkf/rm0clb5dnpRV53LcFHq23T0fTLGDzvyBvrGRTvzKAHQrkKc45/Y7veNG5ZMlE6My5AU/LOwrY/PH0N/eBiimJuJZEsXMhtkeJrgC2KDiraM4rQ2onQwmnoqKCn3G5SyQpQy+6RRqRs+dGG8BEd0rgQwt8E5JbJIY2+nu84pqB01CWM06gFTmEOdtpIAuqYRnpIQgrqlQa/WjCSAqVoii2BRlKabZKGNtLIdqMJdkgC2iciD3fJw/GQtm7kceD6VuBIhoB1ojo+Ozo4vBAmLSILH7SeLWdVtELHfWVeG+pqTgp1iYL9Pj+Fhkjhe/smN4EtkcBLra/lprAtUjjX9Gf2bW4aOyKNg2HPEUjMVn85bNwKKzFZjQWpgum5Z44Aw9L7U6g2TiC/chOKTmU/IEV1HJYQt4F5dfztEZl9SsosSF2XU59+l5q6IaX+/vT7tMRbUuKXBy8P0lJvS6nPD56nJd6REh+cfHP2Q1pywRfYHxVyK0Wxt+Dn5Og/XZB+8qWpwdz+/ybZMDvPglZq5CWSJ0sbieac34lEX5Gk8aQEU47dz2v6xzOa2YpL1zD0KilTWV0jf9fU1ZWUhQEtFK1n9/1lgcJRnykhW2hB0XAmrPUvS1jY0pV0hhcu/Wj+8sgS76p8/nq7Su8y5hDAkc6d2zV1g1Nxn3q3IwMYgPK2pqaxJTwRrgcT4V2rtHZ7uV/bvAq2VYeZe6UE/WGNHKYUvHSliG9RZTsxOFiRA1rXrgJ6SmiqHcyUeR1xojydhY4rlmzrmSAjszMOSnANZzoUrdF5ToDZJFT7cLXVArc9bNxmDnuZkJuc7rPBbqHi50BvvXzwLS55Mn6LS50C4OKSJyO4uNRpEC4u/QwwXLjnRFFc7yErxvww7psJfkmzR3GFXZyMhY+TAAtCBqxCEPl9o7r5G8HJhF0LsJwVLBN2PSzEzNcGhM2qRAvvwx0UUncCIft5iN3rX56UhIcobUPjhpyf7Kp5BpgMFoJrKxutQ9pGdzNKXVvNaysQSWBHhS0/s64wulMjhKxbR3NXrS5RrbGatYvuAIFmZZLDdWo3t07tgk5lRNynzEsAqn9tTaVTr62sSrU0LyXKKvUw1We8yWGhRuemRilmfHBqdDENmLWwFhqgZjMF+HxHKUk9LcaqyFgl8eeuRyx/57XZDVVvTs9FiC+6X8xkaFoCUc+3DU3aSVgDeyCLDlD3hScIgYFkER3zGQ6OKf7aqEcFDSq061eu+lUQ20AVRiIdoi4E9QtSElig4yRDc8d5Nw0ClZLSZEDQlZsM7vAmI17QRDVBKlErkeCmka+VRqZjU7fupbEzyB9N9pRundqkvTttNLSv5cJCdpHgJrLVJTp4X1+WyDVqVKbjqBJN9n1FLWbqaVqstCa8F7TltvVCMwegvZf9mJWL25EhBK2kas7MeYrGkx3rOWEYyZQ2wlpTqS3n3lEy84aSRfWapEwn+CQnCgvqfHU6x11JtR4cHh69idkhjXuwPVzoP0Nc7BTaw4y/8ZTGi5YYKksDwkGoahwaRs/8yyvieY9IgCXmKms1ie8nNt9ihJVoVtB1Prt+mFi/UN2I46YmBZESeJBtLzlUwAA7YThDJYnqHLRx2mxE5j9k7KtfbAKqbnkraKuC5ouNcagxrSl0KjxqRiiSHyrrnxyYQq6O2wCDuE0m97nooLcngvoh2idwkX24+mc66RCa7NyzxZns4cXZq7VDNa15+ZyShQPNdvtFpB4KaScZBRCYCzEmlKd5Pjg2hU5PgZYpLv+w8lKolDrLE4o8NnEbeAwdzzC7E0VLnHJRrCG0CsoWK3fQ0Ya68YH2NYWGSQZzp7atOfrx0AMtMaZRVrE2KGzUkTEzKwLr74lbkM9WpMmE7fjkGxYIlOUYmkfkRTLRQ8f1AIh0x8POQ1YDhcOC2Dbi0wYCMTL80JBp4n+k7efxoMnicT/nhqFYt8xKV6BcUsjPG8fGEFflm7HmzCemBj1UtJ5mRhybZLcmlgQ7s9c3nCm8mNj7RZyYeDmpo45PiDowuZ7mjd3o03r8tvD+c+qgRE+90q7HMfTF6Jp4GtQPqYeNFH04ZWyMWHGGOs4vDi7engtTHl73h6trLLeXZX8jnLMzbqSsK0DrAD1oGyWlE8K4UvKUtqEY1si7nWY0o+NA0PSOkWvPGG4EYkYWHGhWApMvVCQdFYS3rITcs9vDmYrNZRBPR+DntHGCQ6dw10vJFGwHhqkpOS4eKaYcnh0dXBwp35+ePSc7qwtHiPnnYZgzs8ve8w4YkdJLwhTT4aVjPl6YgwFBuX1DweB9EtdJjlOyu+SmR10p2sbAvlHTe4OWbQcNjp+fGyNtKDTvPj1DjAyCbM8HbU1l59vQnSKW2s0cGVwYw57Wj+bQyUPkmTHQrjVQ1REyeh4yb4BEzxzEVdjIQucC39cGyiutbzrKk8CuaHzYV35+/vz16x9++DmGmU3jcnO/jgLWg8v6/hZe9uFya/8qg2wnnQ/TsL7VBrbyb7bVhj/n3x6/UbR3mrL/nuRq5uNMR3OiJX9XjLsJ1K7z85hSyszp4vp10LzmbWTBJWujIVzSNkKB4KeqfeV+5f44xH+Dq8W/0X/Df2dDJe/fL+tfVflKKWuVTkWrtOE//LdDfnXIL3qX3tHhSocrnf0X3NEqBny78O3Btw93Dfh24duDbx9SGPDtwrcH3z68Y8C3C98efPuht7XQ2+3Q253Q27w0XfJ+D+7gVZf8pVd4r8ee9MnfPvnbZenbJE2bXHfIdYdc6+RaJ9daxYTvO/hew5UB33fwvYa3TPi+g+81vGXC9x18ryHFNUn9jjzFuzp838Fdjbx1TVLp8EV6A/ha8B1CigF8Lfji9TVZIr/psdW7mz6Ok2X4/S9KbXOT2m/JU/hnjSwtiZpDg3to6L3prQq72hhDmRr8FqiRp/BPlJrJqAHsFKiRw9Tk0uEdsXw0BfkTparzMsJjkW4vXMyeXE76vBdb0neMZk8uKkkRnH8nhvFXt7OAXiVlpTjlJF3lK5cAGuUrbRqHB3+aIUHPihJMNyOHxBHjvTqDTPlJCdKpZ9SAEMyrv1xgnd8XL+7YPFz8AYYnTHz4Fls/j4LzXJM73MAk+6jhpmzCaen4Uzf5A85Yip2LbmMn9FPS4uRwNWH7taB5Ju1Xl+WQwmk7/8iwTJeEgGSo7zlMNhzNs52U+s5nJdAyrsk6AjKTbKzCGr+i8NaHGpQxVRUUlTkqr65W3dHA9Mqot1glie6nDhuf5bm2vFLpR9uy61kecLscf/gvsIqA8vSDb9OPvUW54257ftGXIz4Y8qrmK3hJ6FZi+Iy6xrm0pv6srnGSywWOhOV6IGfxGhYxehcoH1vQBYWTM8ua9dzMzZCiS77SYdohnYsN0wySBm6I2MzSMdu7lEvNgGuCfz1jfOgFqGMzyDdIDvxCyS2o6eQBl64ynB/8cBBxgX84xqzZbOfK6I0jEYkTlo0JN1NXjXu2rYfc2vrSkjHxwcNUCUvGwjE/vm+eaur0d7cZ2kDd1MV9UumALIUTmlT+uhyX6+KWlanuF69viSu4JJq045qooJXmE/ZT2P25sCWYbiyZFvCLvphMHFkVV/0ci0HtEBMpdBAw/4ywdzmyWl45On1BOuxqIhrn6+YzLIfo8Azy4RiW/d6IdqWAqSW5SKHAgNIMi5bRtzHShT798+/E7ytIiz2NH8adhDxn7egta+E3Z6dkh+1v3h6ciZ6IbEFw/+HssT03l4ADaMr3APmm8Qc4gVpqRehkWCvvTbHiTVcaa2x7RVo+VPKq54yxoEvvtNsyb/WKXwWdryTT9+k6NrRkiyQge1h0NQBhUQpBIpEEW4gOViP5fXLblyAG69hv2o8Nr4WozNT9TLBTh6YeGaINmHM9k4GYdVAK0cemnrhm6Rje2BkqkIQNkaSEcv2NodYmc17c2hpLSujF1WKZTxRK7zXHxLfc5h+QUX9QTbfl9jEACVTyPgxFFZXPRiDbfXWvvfu4tlfrrD/e6urrW1p7Z70NE6b12l67sdfd3NJ22h21opLdtukbUPmK2hmYxtBrWWNP83xa7c1GbUfXd9YbXfhnq23ALM7Qt9bb7fpeZ1vv7Gy1N9U//nGFrQCjf+iKbnfg5WZta3d3c6tR36s3dnZrjxsrwEznlgzOzWP3nFXg3PBesxxXyHyyBUzTxgPPbWIfZPeG48GA3ZCma6zMxEMGaHds3WjCbWAizDVb0H4t6qc2SM2XJQe6A8NpdQYA2uJTltDkTJuwojDsAQ3VB70Hc0xoqz+ooPw9KNI6LvergOhVQD4Ds0Ne3/iwDpOmdZyfrkN3MoZYXl2tKOoBzIBtx/xIkpHXTvGWQq3cvE/8MUvHJrd+GqiRTkx8d+H9isI6Fv6pKEHh2RXXm2LXJtuTS90O24LM+HiqHMu7OUMLBQU8A0eHaFWIqrqTutSs0EAwM8eNdCzBNSbUvUUEodVqNkutlqWZw1artO8fV+TZ9oDexQzY1kD/H7UKqtY=")))