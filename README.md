# RevolX

Multi Threaded Headless Firefox Automation tool for Hack PTC sites.

## Supported Sites

- vuexybux 


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
```

### 4. Run RevolvX
```shell
python revolvx.py
```

### Optional
- You can view firefox UI by setting
``options.headless = False`` in revolx.py file

- Put a star to this repo if you like this.  :hugs: