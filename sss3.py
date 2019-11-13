import logging
logging.basicConfig(format="%(asctime)s:%(levelname)s:%(message)s",datefmt="%d/%m/%Y %I:%M:%S %p")
print("loggging demo")
logging.debug("debug information")
logging.info("info infrmation")
logging.warning("warning information")
logging.error("error information")
logging.critical("critical information")
