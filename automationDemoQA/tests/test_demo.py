from automationDemoQA.src.pages.FillPage import FormPage

ruta = "capture/"
document = "E:/Automatizaciones/Playwright con python/DemoQA1/automationDemoQA/tests/document/serenity.png"


def test_demo(set_up):
    page = set_up
    form = FormPage(page)
    form.enter_name("Pablo", ruta + "Name.png")
    form.enter_lastname("Garcia", ruta + "LastName.png")
    form.enter_email("Garcia1@gmail.com", ruta + "Email.png")
    form.click_gender(ruta + "Gender.png")
    form.enter_mobile("3125484897", ruta + "Mobile.png")
    form.enter_date(ruta + "Date.png")
    form.enter_subjects("Maths", "English", "Physics", ruta + "Subjects.png")
    form.enter_hobbies(ruta + "Hobbies.png")
    form.enter_upload(document, ruta + "Upload.png")
    form.Scroll_x(0, 500)
    form.enter_address("Calle 29 A sur", ruta + "Address.png")
    form.Scroll_x(0, 500)
    form.enter_state_city(ruta + "City.png")
    form.click_submit(ruta + "Submit.png")
    form.assert_text("Thanks for submitting the form", ruta + "Congratulations.png")
