from app.domain.output import Output
from app.domain.organization import Organization
from app.domain.article import Article

class SandboxOutput(Output):
    def __init__(self):
        '''
        コンストラクタ
        '''
        self.organization = None
        self.article = None

    def set_organization(self, organization: Organization):
        '''
        組織情報を代入します
        '''
        self.organization = organization
    
    def set_article(self, article: Article):
        '''
        記事情報を代入します
        '''
        self.article = article
    
    def get_organization(self) -> Organization:
        '''
        組織情報を返します
        '''
        return self.organization
    
    def get_article(self) -> Article:
        '''
        記事情報を返します
        '''
        return self.article