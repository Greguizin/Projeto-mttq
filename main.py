class Leitura:
    def __init__(self, faixa, cor):
        self.faixa = faixa
        self.cor = cor
        
def ldrler():
    num_leituras = 5
    ldr_value = sum(ldr.read() for _ in range(num_leituras))
    ldr.atten(ADC.ATTN_11DB)
    return ldr_value / num_leituras

def rgbcor(z):
    cores = {
        'azul': (0, 0, 255),
        'vermelho': (255, 0, 0),
        'verde': (0, 255, 0)
    }
    cor = cores.get(z)
    if cor is not None:
        np[0] = cor
        np.write()
ldrler()

 
def client_connect():
  global client_id, mqtt_server, topic_sub, server_port, mqtt_user, mqtt_password
  client = MQTTClient(client_id, mqtt_server, server_port, mqtt_user, mqtt_password)
  client.connect()
  print('Connected to %s MQTT broker!' % (mqtt_server))
  return client

def restart_and_reconnect():
  print('Failed to connect to MQTT broker. Reconnecting...')
  time.sleep(10)
  machine.reset()

try:
  client = client_connect()
except OSError as e:
  restart_and_reconnect()

while True:
  try:
    if (time.time() - last_message) > message_interval:
        for cor in cores:
            rgbcor(cor)
            time.sleep(5)
            valor_lido = ldrler()
            teste = Leitura(valor_lido, cor)
            print(teste.faixa, teste.cor)
            msg = b' a cor %s marcou : %d ' % (teste.cor, teste.faixa)
            client.publish(topic_pub, msg)
        last_message = time.time()
        counter += message_interval    
  except OSError as e:
        restart_and_reconnect()




