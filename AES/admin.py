from django.contrib import admin
from .models import EncryptedData

class EncryptedDataAdmin(admin.ModelAdmin):
    list_display = ('id', 'encrypted_data')

    def get_decrypted_data(self, obj):
        client_password = "password"
        encryption_module = SymmetricEncryption(client_password.encode())
        return encryption_module.decrypt(obj.encrypted_data.encode())

    get_decrypted_data.short_description = 'Decrypted Data'

admin.site.register(EncryptedData, EncryptedDataAdmin)