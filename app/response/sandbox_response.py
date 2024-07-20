from pydantic import BaseModel
from typing import Optional

class OrganizationResponse(BaseModel):
    limit: int
    count: int

class ArticleResponse(BaseModel):
    content: str

class SandboxResponse(BaseModel):
    organization: Optional[OrganizationResponse]
    article: Optional[ArticleResponse]