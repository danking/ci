import logging

fmt = logging.Formatter(
    '%(levelname)s:%(asctime)s:%(filename)s:%(funcName)s:%(lineno)d: '
    '%(message)s'
)

fh = logging.FileHandler('ci.log')
fh.setLevel(logging.INFO)
fh.setFormatter(fmt)

ch = logging.StreamHandler()
ch.setLevel(logging.INFO)
ch.setFormatter(fmt)


log = logging.getLogger('ci')
log.setLevel(logging.INFO)
log.addHandler(fh)
log.addHandler(ch)

logging.basicConfig(
    handlers=[fh, ch],
    level=logging.INFO
)
