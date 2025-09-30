import cv2
import numpy as np
import matplotlib.pyplot as plt
import os

# --- Configuração Inicial ---

# Crie uma pasta 'sample_data' e coloque 'Imagem.jpg' dentro dela,
# ou ajuste o caminho para sua imagem.
INPUT_IMAGE_PATH = 'sample_data/Imagem.jpg'
OUTPUT_DIR = 'saidas'

# Garante que o diretório de saída exista
if not os.path.exists(OUTPUT_DIR):
    os.makedirs(OUTPUT_DIR)

# --- Funções dos Exercícios ---

def exercicio_1(img_rgb):
    """
    1 — Canais de Cor (R, G, B): extração e visualização
    """
    print("Executando Exercício 1: Canais de Cor...")

    canal_r = img_rgb[..., 0]
    canal_g = img_rgb[..., 1]
    canal_b = img_rgb[..., 2]

    # 2. Exibir cada canal em tons de cinza
    fig, axes = plt.subplots(1, 3, figsize=(15, 5))
    fig.suptitle('Exercício 1: Canais de Cor (R, G, B)', fontsize=16)

    # Canal Vermelho (R)
    axes[0].imshow(canal_r, cmap='gray')
    axes[0].set_title('Canal Vermelho (R)')
    axes[0].axis('off')

    # Canal Verde (G)
    axes[1].imshow(canal_g, cmap='gray')
    axes[1].set_title('Canal Verde (G)')
    axes[1].axis('off')

    # Canal Azul (B)
    axes[2].imshow(canal_b, cmap='gray')
    axes[2].set_title('Canal Azul (B)')
    axes[2].axis('off')

    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, 'Ex1_Canais.png'))


def exercicio_2(img_rgb):
    """
    2 — Alterações de canais: remoção, troca e reforço
    """
    print("Executando Exercício 2: Alterações de Canais...")
    
    # Criar uma figura para os resultados
    fig, axes = plt.subplots(1, 3, figsize=(15, 5))
    fig.suptitle('Exercício 2: Alterações de Canais', fontsize=16)

    # 1. Remover o canal Azul (B=0)
    img_sem_azul = img_rgb.copy()
    img_sem_azul[..., 2] = 0
    axes[0].imshow(img_sem_azul)
    axes[0].set_title('Canal Azul Removido (B=0)')
    axes[0].axis('off')

    # 2. Trocar os canais R↔B
    img_trocada = img_rgb.copy()
    # Pega o canal R original e o B original
    r_original = img_rgb[..., 0].copy()
    b_original = img_rgb[..., 2].copy()
    # Atribui B para o canal R e R para o canal B
    img_trocada[..., 0] = b_original
    img_trocada[..., 2] = r_original
    axes[1].imshow(img_trocada)
    axes[1].set_title('Canais Vermelho e Azul Trocados (R↔B)')
    axes[1].axis('off')

    # 3. Reforçar o canal Verde em +30%
    img_reforco_verde = img_rgb.copy().astype(np.float32) # Converte para float para evitar overflow
    canal_verde = img_reforco_verde[..., 1]
    # Aumenta em 30% e limita os valores entre 0 e 255
    canal_verde = np.clip(canal_verde * 1.3, 0, 255)
    img_reforco_verde[..., 1] = canal_verde
    # Converte de volta para uint8 para exibição
    img_reforco_verde = img_reforco_verde.astype(np.uint8)
    axes[2].imshow(img_reforco_verde)
    axes[2].set_title('Canal Verde Reforçado em 30%')
    axes[2].axis('off')
    
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, 'Ex2_Alteracoes.png'))


def exercicio_3(img_rgb):
    """
    3 — Transformações geométricas: translação, rotação e escala
    """
    print("Executando Exercício 3: Transformações Geométricas...")
    h, w = img_rgb.shape[:2]
    
    fig, axes = plt.subplots(1, 3, figsize=(15, 5))
    fig.suptitle('Exercício 3: Transformações Geométricas', fontsize=16)

    # 1. Transladar a imagem em (+40 px, +25 px)
    matriz_translacao = np.float32([[1, 0, 40], [0, 1, 25]])
    img_transladada = cv2.warpAffine(img_rgb, matriz_translacao, (w, h))
    axes[0].imshow(img_transladada)
    axes[0].set_title('Translação (+40px, +25px)')
    axes[0].axis('off')

    # 2. Rotacionar a imagem em +20°
    centro = (w // 2, h // 2)
    matriz_rotacao = cv2.getRotationMatrix2D(center=centro, angle=20, scale=1.0)
    img_rotacionada = cv2.warpAffine(img_rgb, matriz_rotacao, (w, h))
    axes[1].imshow(img_rotacionada)
    axes[1].set_title('Rotação (+20°)')
    axes[1].axis('off')

    # 3. Redimensionar (escala 1.5×)
    img_escalada = cv2.resize(img_rgb, None, fx=1.5, fy=1.5, interpolation=cv2.INTER_CUBIC)
    axes[2].imshow(img_escalada)
    axes[2].set_title('Escala (1.5x)')
    axes[2].axis('off')

    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, 'Ex3_Geometricas.png'))


def exercicio_4(img_rgb):
    """
    4 — Cinza (média vs. perceptual) + equalização de histograma
    """
    print("Executando Exercício 4: Escala de Cinza e Equalização...")
    
    fig, axes = plt.subplots(1, 3, figsize=(15, 5))
    fig.suptitle('Exercício 4: Escala de Cinza e Equalização', fontsize=16)
    
    # Trabalhar com float para precisão nos cálculos
    img_float = img_rgb.astype(np.float32)
    r, g, b = img_float[..., 0], img_float[..., 1], img_float[..., 2]

    # 1. Implementar cinza por média
    cinza_media = (r + g + b) / 3.0
    cinza_media = cinza_media.astype(np.uint8)
    axes[0].imshow(cinza_media, cmap='gray')
    axes[0].set_title('Cinza por Média')
    axes[0].axis('off')
    
    # 2. Implementar cinza perceptual
    cinza_perceptual = (r * 0.299 + g * 0.587 + b * 0.114)
    cinza_perceptual = cinza_perceptual.astype(np.uint8)
    axes[1].imshow(cinza_perceptual, cmap='gray')
    axes[1].set_title('Cinza Perceptual (Luminosidade)')
    axes[1].axis('off')
    
    # 3. Comentário sobre as diferenças (no código)
    # A conversão por média trata todos os canais com o mesmo peso.
    # A conversão perceptual (luminosidade) é mais fiel à percepção humana,
    # que é mais sensível ao verde e menos ao azul. Por isso, a imagem
    # perceptual geralmente parece ter um contraste mais natural.

    # 4. Aplicar equalização de histograma na versão perceptual
    cinza_equalizado = cv2.equalizeHist(cinza_perceptual)
    axes[2].imshow(cinza_equalizado, cmap='gray')
    axes[2].set_title('Perceptual com Equalização')
    axes[2].axis('off')
    
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, 'Ex4_Cinza_Eq.png'))


def exercicio_5(img_rgb):
    """
    5 — Cisalhamento (shear) e recorte (crop)
    """
    print("Executando Exercício 5: Cisalhamento e Recorte...")
    h, w = img_rgb.shape[:2]

    # 1. Implementar cisalhamento horizontal com fator Sx = 0.3
    fator_sx = 0.3
    matriz_shear = np.float32([[1, fator_sx, 0], [0, 1, 0]])
    # Adiciona espaço extra na largura para ver o efeito completo
    img_cisalhada = cv2.warpAffine(img_rgb, matriz_shear, (int(w + h * fator_sx), h))

    # 2. Realizar um recorte central de 60%
    crop_h, crop_w = int(h * 0.6), int(w * 0.6)
    start_h = (h - crop_h) // 2
    start_w = (w - crop_w) // 2
    img_recortada = img_rgb[start_h : start_h + crop_h, start_w : start_w + crop_w]

    # 3. Salvar as duas versões
    # OpenCV salva em BGR, então convertemos de RGB para BGR antes de salvar.
    cv2.imwrite(os.path.join(OUTPUT_DIR, 'Ex5_Cisalhamento.jpg'), cv2.cvtColor(img_cisalhada, cv2.COLOR_RGB2BGR))
    cv2.imwrite(os.path.join(OUTPUT_DIR, 'Ex5_Recorte.jpg'), cv2.cvtColor(img_recortada, cv2.COLOR_RGB2BGR))
    print(f"Imagens de cisalhamento e recorte salvas em '{OUTPUT_DIR}/'.")
    
    # Montar uma figura comparativa
    fig, axes = plt.subplots(1, 3, figsize=(18, 6))
    fig.suptitle('Exercício 5: Comparativo Final (Original, Shear, Crop)', fontsize=16)

    # Original
    axes[0].imshow(img_rgb)
    axes[0].set_title('Original')
    axes[0].axis('off')

    # Shear
    axes[1].imshow(img_cisalhada)
    axes[1].set_title('Cisalhamento (Shear)')
    axes[1].axis('off')

    # Crop
    axes[2].imshow(img_recortada)
    axes[2].set_title('Recorte (Crop)')
    axes[2].axis('off')
    
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, 'Ex5_Comparativo.png'))


# --- Execução Principal ---

def main():
    """
    Função principal que carrega a imagem e chama os exercícios.
    """
    # Tenta ler a imagem
    # O OpenCV carrega em formato BGR por padrão.
    img_bgr = cv2.imread(INPUT_IMAGE_PATH)

    # Verifica se a imagem foi carregada corretamente
    if img_bgr is None:
        print(f"Erro: Não foi possível carregar a imagem em '{INPUT_IMAGE_PATH}'.")
        print("Verifique se o caminho está correto e se o arquivo existe.")
        return

    # Converte de BGR para RGB para trabalhar com Matplotlib e por consistência
    img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)

    # Chama cada função de exercício
    exercicio_1(img_rgb)
    exercicio_2(img_rgb)
    exercicio_3(img_rgb)
    exercicio_4(img_rgb)
    exercicio_5(img_rgb)
    
    # Mostra todos os gráficos gerados pelo Matplotlib
    print("\nProcessamento concluído. Exibindo todos os resultados...")
    plt.show()


if __name__ == '__main__':
    main()

