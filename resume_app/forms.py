from django import forms

class ResumeForm(forms.Form):
    resume_file = forms.FileField(label="Upload Resume (PDF or DOCX)")
    job_desc_text = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 6}),
        label="Paste Job Description"
    )

from django import forms

class ResumeForm(forms.Form): 
    resume_file = forms.FileField(label="Upload Resume (PDF or DOCX)") 
    job_desc_text = forms.CharField( widget=forms.Textarea(attrs={'rows': 6, 'placeholder':'Paste job description here'}), 
    label="Job Description" 
    )

class CoverLetterForm(forms.Form): 
    job_description = forms.CharField( widget=forms.Textarea(attrs={'rows': 8, 'placeholder':'Write or copy/paste your job description…'}), 
    label="Job Description" ) 
    resume = forms.FileField( label="Upload Resume (optional)", required=False )