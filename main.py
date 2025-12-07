import os
import google.generativeai as genai

# -----------------------------------------------------------
# إعداد الاتصال بـ Gemini
# ملاحظة هامة: لا تقم أبداً بكتابة مفتاحك مباشرة هنا ورفعه
# سنقوم بجلب المفتاح من متغيرات النظام للحفاظ على الأمان
# -----------------------------------------------------------

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    print("خطأ: لم يتم العثور على مفتاح API.")
    print("تأكد من إعداد متغير البيئة GEMINI_API_KEY")
else:
    try:
        # إعداد المكتبة بالمفتاح
        genai.configure(api_key=api_key)

        # اختيار الموديل (Flash هو الأسرع والأخف)
        model = genai.GenerativeModel('gemini-1.5-flash')

        # إرسال رسالة تجريبية
        prompt = "مرحباً يا Gemini! هل يمكنك تعريفي بنفسك في جملة واحدة؟"
        print(f"جاري إرسال السؤال: {prompt} ...\n")

        response = model.generate_content(prompt)
        
        # طباعة الرد
        print("رد Gemini:")
        print(response.text)

    except Exception as e:
        print(f"حدث خطأ أثناء الاتصال: {e}")
