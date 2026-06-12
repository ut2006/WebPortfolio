from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['full_name', 'email', 'phone', 'subject', 'message']
        widgets = {
            'full_name': forms.TextInput(attrs={
                'class': 'form-control rounded',
                'placeholder': 'Nguyễn Văn B',
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control rounded',
                'placeholder': 'email@example.com',
            }),
            'phone': forms.TextInput(attrs={
                'class': 'form-control rounded',
                'placeholder': '0901 ...',
            }),
            'subject': forms.TextInput(attrs={
                'class': 'form-control rounded',
                'placeholder': 'Chủ đề muốn trao đổi',
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-control rounded',
                'rows': 4,
                'placeholder': 'Nội dung tin nhắn...',
            }),
        }
        labels = {
            'full_name': 'Họ tên',
            'email': 'Email',
            'phone': 'Số điện thoại (tùy chọn)',
            'subject': 'Tiêu đề',
            'message': 'Nội dung',
        }
