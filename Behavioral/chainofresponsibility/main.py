class Handler:
    def __init__(self, successor=None):
        self._successor = successor

    def handle_request(self, request):
        if self._successor is not None:
            self._successor.handle_request(request)

class Manager(Handler):
    def handle_request(self, request):
        if request.is_complete():
            print("Dokumen disetujui oleh manajer.")
        else:
            print("Dokumen belum lengkap. Diteruskan ke atasan.")
            super().handle_request(request)

class DepartmentHead(Handler):
    def handle_request(self, request):
        if request.is_compliant():
            print("Dokumen sesuai dengan kebijakan departemen. Diteruskan ke direktur.")
            super().handle_request(request)
        else:
            print("Dokumen tidak sesuai dengan kebijakan departemen.")

class Director(Handler):
    def handle_request(self, request):
        if request.is_financially_sound():
            print("Dokumen disetujui oleh direktur.")
        else:
            print("Dokumen tidak disetujui karena alasan finansial.")

# Contoh penggunaan
request = DocumentRequest()  # Simulasi dokumen yang akan diajukan
manager = Manager()
department_head = DepartmentHead(manager)
director = Director(department_head)

director.handle_request(request)
