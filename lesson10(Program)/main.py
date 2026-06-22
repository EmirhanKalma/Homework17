


# students = ["Emirhan" , "Vaci" , "Himan" , "Beron" , "Nuner" , "Ranew"]

filename = input("Введите название файла: ")

filename_list = filename.split(".")
image_extensions = [
    'jpg', 'jpeg', 'png', 'gif', 'webp', 'svg', 'svgz', 'ico', 'bmp', 'avif', 'heic', 'heif', 'jfif', 'pjpeg', 'pjp', 'apng','tiff', 'tif', 'raw', 'arw', 'cr2', 'cr3', 'crw', 'dng', 'nef', 'nrw', 'orf', 'pef', 'raf', 'rw2', 'sr2', 'srf', 'x3f', 'mrw', 'erf', 'kdc', 'mos','psd', 'psb', 'ai', 'eps', 'indd', 'cdr', 'cgm', 'emf', 'wmf', 'dwg', 'dxf','exr', 'hdr', 'dds', 'tga', 'icb', 'vda', 'vst','jp2', 'j2k', 'jpf', 'jpx', 'jpm', 'mj2', 'jxl', 'bpg', 'flif','wbmp', 'xbm', 'xpm', 'pbm', 'pgm', 'ppm', 'pnm', 'pcx', 'pict', 'pct', 'pic', 'sgi', 'rgb', 'rgba', 'bw', 'int', 'inta', 'djvu', 'djv', 'dib', 'mac', 'mpo', 'ani', 'cur'
]
if filename_list[-1] in image_extensions:
    print(f"{filename} является картинкой")
else:
    print(f"{filename} не является картинкой")



polindrom = input("Введите ваше слово: ").strip()
polindrom_first = polindrom[0].lower()
polindrom_last = polindrom[-1].lower()
if polindrom_first == polindrom_last:
    print(f"{polindrom} является полиндромом")
else:
    print(f"{polindrom} не является полиндромом")