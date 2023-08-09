from django.shortcuts import render
from .encryption_module import SymmetricEncryption  # 암호화 모듈 임포트


def encrypt_data(request):
    client_password = "user123"  # 사용자 비밀번호
    encryption_module = SymmetricEncryption(client_password.encode())

    original_data = "Sensitive information."
    encrypted_data = encryption_module.encrypt(original_data)

    return render(request, 'encrypted_data.html', {'encrypted_data': encrypted_data})