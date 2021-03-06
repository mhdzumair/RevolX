# RevolX

Multi Threaded Headless Firefox Automation tool for Hack PTC sites.

## Supported Sites

- [vuexybux](https://vuexybux.com/)


## Requirement

- Install [python 3.7+](https://www.python.org/downloads/)
- [Firefox Browser](https://www.mozilla.org/en-US/firefox/new/)
- Install Firefox [geckodriver](https://github.com/mozilla/geckodriver/releases) for your platform. [ Linux, Windows driver already added here.]
- [Resolvo Pro](https://github.com/mhdzumair/ResolvoPro.git)
- [Ads Fucker](https://github.com/mhdzumair/ads_fucker) [ Already added Here. ]


## Usage

### 1. Open sites.xml file and configure your accounts.
Note: You can add many accounts as you wish.

```xml
<?xml version="1.0" encoding="utf-8" ?>
<sites>
    <site name="vuexybux">
        <username>mhdzumair</username>
        <password>Password</password>
    </site>
    <site name="vuexybux">
        <username>mhdzumair@gmail.com</username>
        <password>Password123</password>
    </site>
</sites>
```

### 2. Install RevolX Dependency
```shell
pip install -r requirment.txt
```

### 3. Download & Run ResolvoPro
Note: open another terminal & download ResolvoPro
```shell
git clone https://github.com/mhdzumair/ResolvoPro.git
cd ResolvoPro/
pip install -r requirments.txt
python fastapp.py

# if you have issue with opencv in linux
sudo apt install python3-opencv
```

### 4. Run RevolvX
```shell
python revolvx.py
```

### Optional
- You can view firefox UI by setting
``options.headless = False`` in revolx.py file

- Put a star to this repo if you like this.  :hugs:

- Setup Socks5 Proxy

```python
profile = webdriver.FirefoxProfile()
profile.set_preference('network.proxy.type', 1)
profile.set_preference('network.proxy.socks', "127.0.0.1")
profile.set_preference('network.proxy.socks_port', 1080)
profile.set_preference("network.proxy.socks_version", 5)
profile.set_preference("network.proxy.socks_remote_dns", True)

# setup driver firefox profile. 
webdriver.Firefox(executable_path=geckodriver, options=options, firefox_profile=profile)
```
