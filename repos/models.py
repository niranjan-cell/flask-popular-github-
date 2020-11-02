class GitHubRepo:

# This class is use to represent a single github repository
    def __init__(self,name,language,num_star):
        self.name=name
        self.language=language
        self.num_star=num_star
    def __str__(self):
        return f"->{self.name} is a {self.language} repo with{self.num_star}"
    
    def __repr__(self):
        return f'GitHubRepo({self.name}{self.language}{self.num_star})'