# reCAPTCHA-V2-Bypass (Invisible-Only)

Simple lightweight reCAPTCHA V2 Invisible bypass using the `/reload` feature to obtain valid captcha tokens.

---

## ⚠️ Disclaimer

This tool is provided **for educational and research purposes only**. This is **strictly a demo** and should **not** be used on any website without explicit permission from the owner.

Bypassing reCAPTCHA may violate the terms of service of the target site and Google. Use responsibly and at your own risk.

---

## How It Works

This bypass works because it mimics the internal flow Google uses for **invisible** reCAPTCHA v2. It fetches an initial token from the anchor endpoint and then uses the large background payload (`bg`) to request a solved token via the reload endpoint.

It is **specific to invisible reCAPTCHA** only and does **not** work on checkbox/image challenges or Enterprise versions.

---

## Installation

```bash
pip install requests colorlog
```


## How to Obtain the Required Fields

1. Press **F12** → Go to the **Network** tab.
2. Trigger the invisible reCAPTCHA on the target page.
3. Filter requests by typing `reload`.
4. Click on the `https://recaptcha.net/recaptcha/api2/reload` request.

- **reload_url** → Copy the full request URL.
- **anchor_url** → Scroll to **Headers** → Copy the **Referer** value.
- **bgDATA** → Go to **Payload** tab:
  - Ignore the first line.
  - Search for the first `*` (`Ctrl + F`).
  - Copy everything **before** that `*` (should start with `!03AFcWeA6pB...`).

These values usually remain valid for a long time.

---

## Limitations & What Won't Work

- Does **not** work if you see `/bframe` in the endpoints
- Does **not** work with **reCAPTCHA Enterprise**
- Does **not** work with visible checkbox challenges
- Only works on **invisible** reCAPTCHA v2 implementations

---

## Legal & Ethical Warning

Always obtain permission from the website owner before using this tool on their site. Unauthorized use may be illegal.

---

**For research and educational purposes only.**



## Usage Example

See `demo.py` for a full working example:

```python
from solve import reCAPTCHASolver

reloadURL = 'https://recaptcha.net/recaptcha/api2/reload?k=6LeXd3cbAAAAAFwQ_UtyHowlKKhJhfMjGPZFXjqr'
anchorURL = 'https://recaptcha.net/recaptcha/api2/anchor?ar=1&k=6LeXd3cbAAAAAFwQ_UtyHowlKKhJhfMjGPZFXjqr&co=aHR0cHM6Ly9jb3Jwb3JhdGVnaWZ0LmNvbTo0NDM.&hl=id&v=A7KpaEASfhDcK0nXxgQEyyYv&size=invisible&anchor-ms=20000&execute-ms=30000&cb=anifmgn2a798'

bgDATA = '!03AFcWeA6pBmj7JYd8HmP0WifEi6IMY2J65vZZVkw-DhD7EC6ACm22vFax61zpVYCV0SG4CVC1purlAeoO6-Q2vT8xhSBXF1SFWydxq6FZ5PVJ2vh4OI9f_UiYIFvnBYNF5b2ptPCWMCOaoauuGj3TAnBbvgR5msvjr_0UtbNAsytfUzJz2VGKeZ0ak2ZEAIoj9VBkQBpDslNcbVDUPdvGoUXKXdv4nv6E879-xgU-2WiNU1PMfe5NZMZRm1bjvGdX-8VekdW-t0VQnHLcm92-rdpe9lv9N41IGq-c6oM_kjS55pJB9II1hCqNROq9KMdD4FH2AQegHR1EkxM8mztTyoVGoQ5D0s1BvfgkuZFJWqoALYVk7gk9MnpI3xG6hfpWocL0iY2TEOJBBfpUs1M2GMfQ2z0as_DBeWScPf8KaTjR-2X2sZmFcns1CgTK0QV-3nfBhSdOhiUnhaSMvHt3Ev0vgZUGpqNfh4MWsUz6ySlkyJsLuRPKq9IL5AOu7-L2M7FMxVi9AuFa5g9UCg9QikRczwajKGccYTLmScByKXlX0-jtmDwjVx-jVPGP_DJNwSTrrxTEbS44_98b2LsjE1NZuE3axWX8kW1LX-92xWG0wr5YFbKSi1ZAujqxdvnaxz169wL9nGY2DWDez8txqGYzNceXnEh6rcyPnphZ4AnuaHInwEkkXt6wr4oDerclbD_DDOFoDSFOVfM7nQNe1fGuGfhgIciKtaAWk2XS8rrsXxKfDZesfdHP29tnsAy9za7McmmLE1NGrY25jQJylOsIEvhMBc_hX3AoJqbFMBgXSFPSXHCxlsrst6Nh5-AHmCQD8iApgDQFR-BEx7zOHjIC6DOMOPg02AUxXRlQvNWlsrBf1nCLbgiFyDsVWZSidSWOIUpuCeA4kcaHFfpNk_mum2mHklPqWe2s-ENbtZnrCbTwjNXTPbLMf1SIG3JGZPJli8TNkLvlO1ljHU0d77milkT4SjJck0zaffNnUJytBqMSE5nSIG80JrS7dFi4oApCiPoXBDJWMveIlgY0iG24r4erGYhjayqLBCf7nTvXFLSVgOZAFRee43k54HW2-zXBJknkx4UTrZZCqYODTWKSpXecXhxWBu3SitkozcOsot80Vs1IruxgnDOOZyWdRbsIpYNA95KwFJUs-80I1S9XN5C_CWCiRujIvGVueiNLq0kuBnLxJvRv2WSudzNtUi5k19WZSIKqlfm-f6ttH-3jTJhtJSx5U2tuAXDkwyEDHtW7HWaT3j2Ha6NOEB-Z30T1fXf2Rl4JBxCCwwf4Dubw2QObWtTlSIsAdJwEYa4cwqsk6XKi25-dVEHQKhvShl58tgt9Nuds_9QMsdHLnbU3V4moeu-L7c9qbJh_yXTnFMc3ACVkLosW9JWECKEt0E2i_y1-CpCCUAAFkTCjfsoBsd_3o9CP6gYUHF0asP3Zu3n5TRh5GzFbci38ro1lyAfGjzgbnMcZY24pwG9eVsizmiSiesmn2mr0IEXw4JTzaYOXkz6j28_IYJfFEVNrH2L6wlcl99ukQocbknas_VHQ88KpjQ7H6fye6u3tL9iHZ_p2s9FXrTFjZOTm_Z3wrhmbIZ4-Ahohj7ljioOwl6hd_9MXHt3jhgnaBh9uaWPAXJhgsxKPp_3sCJyNUjWaVMzuo8RYo-R_2mJ6z15Sav09hgHh95xL_Upk8q1NB7wPROXRxk1wKFueGYuDRNqHgi0BqC8R09vT1ip6cSUcIEL1o5uyKbsfqy4NhZY4SeHiDfeBm4zKyWY'

Solver = reCAPTCHASolver(reload_url=reloadURL, anchor_url=anchorURL, bg_value=bgDATA)

CaptchaToken = Solver.solve_reCAPTCHA()

if CaptchaToken:
    print('[+] Solved reCAPTCHA Demo Successfully')
    print(f'[!] Value: {CaptchaToken}')
else:
    print('[-] Failed to solve reCAPTCHA Demo')

```

<img width="1242" height="219" alt="image" src="https://github.com/user-attachments/assets/cfb2ba74-0105-4e9a-880a-3e65c63d690e" />

