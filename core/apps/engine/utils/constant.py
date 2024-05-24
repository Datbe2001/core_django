from enum import Enum


class AppStatus(Enum):
    USER_LOGOUT_SUCCESS = 'USER_LOGOUT_SUCCESS', 200, "User logout successfully."
    DELETE_ACCOUNT_SUCCESS = "DELETE_ACCOUNT_SUCCESS", 200, "Delete account successfully."

    COMING_SOON = "COMING_SOON", 400, "Coming soon."
    REGISTER_USER_FAIL = "REGISTER_USER_FAIL", 400, "Register user failed."
    EMAIL_ALREADY_EXIST = "EMAIL_ALREADY_EXIST", 400, "Email already exist."
    ROOT_NAME_ALREADY_EXIST = "ROOT_NAME_ALREADY_EXIST", 400, "Root name already exist."
    EXPIRED_VERIFY_CODE = "EXPIRED_VERIFY_CODE", 400, "Your code is expired."
    INVALID_VERIFY_CODE = "INVALID_VERIFY_CODE", 400, "Your code is invalid."
    ACCOUNT_IS_LOCKED = "ACCOUNT_IS_LOCKED", 400, "Your account is locked."

    CURRENT_PASSWORD_INCORRECT = "CURRENT_PASSWORD_INCORRECT", 400, "Current password is incorrect."
    PASSWORDS_ARE_NOT_THE_SAME = "PASSWORDS_ARE_NOT_THE_SAME", 400, "Password and password confirm are not the same."
    USER_NOT_HAVE_ENOUGH_PERMISSION = "USER_NOT_HAVE_ENOUGH_PERMISSION", 400, "User does not have enough permission."
    ACCOUNT_HAS_BEEN_DELETED_BEFORE = "ACCOUNT_HAS_BEEN_DELETED_BEFORE", 400, "The account has been deleted before."

    EMAIL_NOT_EXIST = "EMAIL_NOT_EXIST", 404, "Email does not exist."
    USER_NOT_EXIST = "USER_NOT_EXIST", 404, "User does not exist."
    REFERRAL_CODE_NOT_EXISTS = "REFERRAL_CODE_NOT_EXISTS", 404, "Referral code does not exist."
    TOO_MANNY_REQUESTS = "TOO_MANNY_REQUESTS", 429, "Too many requests, please try again later."

    @property
    def message(self):
        return {
            'message': str(self.value[2]),
            'code': str(self.value[1]),
            'data': 'success' if self.value[1] in [200, 201] else 'failed'
        }
