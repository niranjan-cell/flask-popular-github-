# class GitHubApiException(Exception):
#     def __init__(self,status_code):
#         if status_code == 403:
#             message = "The Status Code Reached"
#         else:
#             message=f" The status Code is {status_code}"
#         super().__init__(message)
        
"""
GitHub API Application: Custom Exception Classes
"""

class GitHubApiException(Exception):

    def __init__(self, status_code):
        if status_code == 403:
            message = "Rate limit reached. Please wait a minute and try again."
        else:
            message = f"HTTP Status Code was: {status_code}."

        super().__init__("A GitHub API Error Occurred: " + message)
