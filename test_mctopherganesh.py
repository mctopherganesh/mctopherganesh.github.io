import logging
import datetime


logging.basicConfig (filename='app.log', filemode='w',
                    format='%(name)s - %(levelname)s - %(message)s')
logging.warning('done testing.'+ ', ' + str(datetime.datetime.now()))