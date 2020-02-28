from selenium import webdriver
import time


class WhatsappBot:
    def __init__(self):
        self.mensagem = " Bom dia pessoal, veja o video que acabou de sair https://www.youtube.com"
        self.grupos = ["GRUPO DA FAMÍLIA", "GRUPO DE VENDAS"]
        options = webdriver.ChromeOptions()
        options.add_argument('lang=pt-br')
        self.driver = webdriver.Chrome(executable_path=r'./chromedriver.exe')

    def EnviarMensagens(self):
        # <span dir="auto" title="GRUPO DA FAMÍLIA" class="_19RFN _1ovWX">GRUPO DA FAMÍLIA</span>
        # <div tabindex="-1" class="_13mgZ">
        # <span data-icon="send" class="">
        print('sdufhdsuhfu')
        self.driver.get('https://web.whatsapp.com')
        time.sleep(30)
        for grupo in self.grupos:
            grupo = self.driver.find_element_by_xpath(
                f"//span[@title='INSIRA O NOME DO GRUPO AQUI']")
            time.sleep(3)
            grupo.click()
            chat_box = self.driver.find_element_by_class_name('_13mgZ')
            time.sleep(3)
            chat_box.click()
            chat_box.send_keys(self.mensagem)
            botao_enviar = self.driver.find_element_by_xpath(
                "//span[@data-icon='send']")
            time.sleep(3)
            botao_enviar.click()
            time.sleep(5)


bot = WhatsappBot()
bot.EnviarMensagens()
