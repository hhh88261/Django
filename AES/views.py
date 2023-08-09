from django.shortcuts import render, redirect
from .encryption_module import SymmetricEncryption
from .models import EncryptedData

def encrypt_data(request):
    client_password = "password"
    encryption_module = SymmetricEncryption(client_password.encode())
    
    original_data = "Sensitive information."
    encrypted_data = encryption_module.encrypt(original_data)
    
    EncryptedData.objects.create(encrypted_data=encrypted_data)
    
    return redirect('admin_page')
