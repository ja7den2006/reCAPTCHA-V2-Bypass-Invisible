import requests
import urllib.parse
import colorlog

class reCAPTCHASolver:
    def __init__(self, reload_url, anchor_url, bg_value):
        self.reload_url = reload_url.strip()
        self.anchor_url = anchor_url.strip()
        self.bg_value = bg_value.strip()

        self.site_key = self.anchor_url.split('k=')[1].split("&")[0]
        self.co = self.anchor_url.split("co=")[1].split("&")[0]
        self.v = self.anchor_url.split("v=")[1].split("&")[0]

        self.chr_value, self.vh_value = self.extract_chr_vh(bg_value)

        self.logger = self.setup_logger()

    def setup_logger(self):
        logger = colorlog.getLogger()
        handler = colorlog.StreamHandler()
        handler.setFormatter(colorlog.ColoredFormatter(
            '%(log_color)s%(asctime)s - %(levelname)s - %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'))
        logger.addHandler(handler)
        return logger

    def extract_chr_vh(self, bg_value):
        chr_start_index = bg_value.find("chr=") + 4
        chr_end_index = bg_value.find("&", chr_start_index)
        chr_value = urllib.parse.unquote(bg_value[chr_start_index:chr_end_index])

        vh_start_index = bg_value.find("vh=") + 3
        vh_end_index = bg_value.find("&", vh_start_index)
        vh_value = urllib.parse.unquote(bg_value[vh_start_index:vh_end_index])

        return chr_value, vh_value

    def send_get_request(self, url):
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        else:
            return None

    def send_post_request(self, url, token):
        payload = {
            "v": self.v,
            "reason": "q",
            "c": token,
            "k": self.site_key,
            "co": self.co,
            "hl": "en",
            "size": "invisible",
            "chr": self.chr_value,
            "vh": self.vh_value,
            "bg": self.bg_value
        }
        response = requests.post(url, data=payload)
        if response.status_code == 200:
            return response.text
        else:
            return None

    def solve_reCAPTCHA(self):
        request_text = self.send_get_request(self.anchor_url)
        if request_text:
            token = request_text.split('recaptcha-token" value="')[1].split('">')[0]
            response_text = self.send_post_request(self.reload_url, token)
            if response_text:
                try:
                    captcha_value = str(response_text.split('"rresp","')[1].split('"')[0])
                    return captcha_value
                except Exception as e:
                    return False
            else:
                return False
        else:
            return False

        


