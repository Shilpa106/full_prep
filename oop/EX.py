import getpass
import os
DEV = 'dev'
PROD = 'prod'
DEVELOPERS = ['sunil', 'ankit','vinay', 'balumatta', 'arun-ghontale','vinayjain', 'jassimmohamed', 'jassim', 'zohairshaikh', 'baliram', 'User', 'HP']

EMAIL_FROM = 'mailer@kait.ai'

DEPLOYMENTS = [DEV, PROD]
VALID_ENVIRONMENTS = DEVELOPERS + DEPLOYMENTS
ENVIRONMENT = os.environ.get('KAIT_ENV', getpass.getuser())
print(ENVIRONMENT)