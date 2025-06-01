import cv2
import mediapipe as mp
import speech_recognition as sr
import threading
import time


# MediaPipe para mãos
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1)
mp_draw = mp.solutions.drawing_utils

# Flags de alerta
alerta_gesto = False
alerta_voz = False


# FUNÇÃO – ALERTA

def gerar_alerta(motivo):
    print(f"\n🚨 ALERTA ATIVADO POR {motivo.upper()} 🚨\n")

# THREAD – RECONHECIMENTO DE VOZ

def reconhecimento_voz():
    global alerta_voz
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("[Voz] Sistema de voz ativado. Diga 'socorro' ou 'ajuda' para disparar o alerta.")
        while True:
            try:
                audio = r.listen(source, timeout=5)
                comando = r.recognize_google(audio, language='pt-BR').lower()
                print(f"[Voz] Você disse: {comando}")
                if "socorro" in comando or "ajuda" in comando:
                    alerta_voz = True
                    gerar_alerta("voz")
                    time.sleep(5) 
            except sr.UnknownValueError:
                pass
            except sr.WaitTimeoutError:
                pass
            except Exception as e:
                print(f"[Voz] Erro: {e}")


# THREAD – RECONHECIMENTO DE GESTO

def reconhecimento_gesto():
    global alerta_gesto
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frame = cv2.flip(frame, 1)
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        resultado = hands.process(rgb)

        if resultado.multi_hand_landmarks:
            for mao in resultado.multi_hand_landmarks:
                mp_draw.draw_landmarks(frame, mao, mp_hands.HAND_CONNECTIONS)

                dedo_indicador = mao.landmark[8]
                pulso = mao.landmark[0]

                altura_dedo = dedo_indicador.y
                altura_pulso = pulso.y

                if altura_dedo < altura_pulso:  # Mão levantada
                    alerta_gesto = True
                    gerar_alerta("gesto (mão levantada)")
                    time.sleep(5)  # Evita múltiplos alertas seguidos

       
        cv2.putText(frame, 'Aguarde gesto ou voz...', (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)
        cv2.imshow('Lumina Signal - Gesto', frame)

        if cv2.waitKey(1) & 0xFF == 27: 
            break

    cap.release()
    cv2.destroyAllWindows()

# INICIAR THREADS
if __name__ == "__main__":
    print("===== LUMINA SIGNAL ATIVADO =====")
    print("Pressione 'ESC' na janela de vídeo para encerrar.\n")

    # Criar threads para voz e gesto
    t1 = threading.Thread(target=reconhecimento_voz)
    t2 = threading.Thread(target=reconhecimento_gesto)

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("===== SISTEMA ENCERRADO =====")
