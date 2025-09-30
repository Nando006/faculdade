import cv2
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import os

# Criar diretório para salvar as imagens se não existir
os.makedirs("resultados", exist_ok=True)

def exercicio_1_redimensionamento(img_path):
    """
    Exercício 1 - Redimensionamento e Resolução
    """
    print("=== EXERCÍCIO 1 - REDIMENSIONAMENTO E RESOLUÇÃO ===")
    
    # Carregar imagem colorida com OpenCV
    img = cv2.imread(img_path)
    if img is None:
        print(f"Erro: Não foi possível carregar a imagem {img_path}")
        return
    
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    altura_orig, largura_orig = img.shape[:2]
    
    print(f"Imagem original: {largura_orig}x{altura_orig}")
    
    # Diferentes proporções de redução
    proporcoes = [0.5, 0.25, 0.1]
    
    fig, axes = plt.subplots(2, 2, figsize=(12, 10))
    axes = axes.flatten()
    
    # Mostrar imagem original
    axes[0].imshow(img_rgb)
    axes[0].set_title("Original")
    axes[0].axis('off')
    
    for i, prop in enumerate(proporcoes):
        # Redimensionar
        nova_largura = int(largura_orig * prop)
        nova_altura = int(altura_orig * prop)
        
        img_reduzida = cv2.resize(img, (nova_largura, nova_altura), interpolation=cv2.INTER_AREA)
        img_reduzida_rgb = cv2.cvtColor(img_reduzida, cv2.COLOR_BGR2RGB)
        
        # Mostrar
        axes[i+1].imshow(img_reduzida_rgb)
        axes[i+1].set_title(f"{int(prop*100)}% ({nova_largura}x{nova_altura})")
        axes[i+1].axis('off')
        
        # Salvar
        cv2.imwrite(f"resultados/ex1_reduzida_{int(prop*100)}.jpg", img_reduzida)
        print(f"Salva: reduzida_{int(prop*100)}.jpg - {nova_largura}x{nova_altura}")
    
    plt.tight_layout()
    plt.savefig("resultados/ex1_comparacao_redimensionamento.png")
    plt.show()

def exercicio_2_amostragem(img_path):
    """
    Exercício 2 - Amostragem
    """
    print("\n=== EXERCÍCIO 2 - AMOSTRAGEM ===")
    
    img = cv2.imread(img_path)
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    altura_orig, largura_orig = img.shape[:2]
    
    # Criar versão de baixa resolução (32x32)
    img_baixa_res = cv2.resize(img, (32, 32), interpolation=cv2.INTER_NEAREST)
    
    # Reampliar para tamanho original
    img_reampliada = cv2.resize(img_baixa_res, (largura_orig, altura_orig), interpolation=cv2.INTER_NEAREST)
    img_reampliada_rgb = cv2.cvtColor(img_reampliada, cv2.COLOR_BGR2RGB)
    
    # Mostrar comparação
    fig, axes = plt.subplots(1, 3, figsize=(15, 5))
    
    axes[0].imshow(img_rgb)
    axes[0].set_title("Original")
    axes[0].axis('off')
    
    img_baixa_rgb = cv2.cvtColor(img_baixa_res, cv2.COLOR_BGR2RGB)
    axes[1].imshow(img_baixa_rgb)
    axes[1].set_title("Baixa Resolução (32x32)")
    axes[1].axis('off')
    
    axes[2].imshow(img_reampliada_rgb)
    axes[2].set_title("Reampliada (efeito aliasing)")
    axes[2].axis('off')
    
    # Salvar
    cv2.imwrite("resultados/ex2_baixa_resolucao.jpg", img_baixa_res)
    cv2.imwrite("resultados/ex2_reampliada.jpg", img_reampliada)
    
    plt.tight_layout()
    plt.savefig("resultados/ex2_comparacao_amostragem.png")
    plt.show()
    
    print("Salvas: baixa_resolucao.jpg e reampliada.jpg")
    print("Efeito de aliasing visível na imagem reampliada")

def exercicio_3_quantizacao(img_path):
    """
    Exercício 3 - Quantização
    """
    print("\n=== EXERCÍCIO 3 - QUANTIZAÇÃO ===")
    
    img = cv2.imread(img_path)
    # Converter para escala de cinza
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # Diferentes níveis de quantização
    niveis = [2, 4, 16, 256]  # 1, 2, 4, 8 bits respectivamente
    
    fig, axes = plt.subplots(2, 2, figsize=(12, 10))
    axes = axes.flatten()
    
    for i, nivel in enumerate(niveis):
        # Quantização
        step = 256 // nivel
        img_quantizada = (gray // step) * step
        
        # Mostrar
        axes[i].imshow(img_quantizada, cmap='gray', vmin=0, vmax=255)
        bits = int(np.log2(nivel))
        axes[i].set_title(f"{nivel} níveis ({bits} bit{'s' if bits > 1 else ''})")
        axes[i].axis('off')
        
        # Salvar
        cv2.imwrite(f"resultados/ex3_quantizada_{nivel}_niveis.jpg", img_quantizada)
        print(f"Salva: quantizada_{nivel}_niveis.jpg")
    
    plt.tight_layout()
    plt.savefig("resultados/ex3_comparacao_quantizacao.png")
    plt.show()
    
    print("Efeito de banding mais visível com menos níveis")

def exercicio_4_remocao_canais(img_path):
    """
    Exercício 4 - Remoção de canais de cor
    """
    print("\n=== EXERCÍCIO 4 - REMOÇÃO DE CANAIS DE COR ===")
    
    img = cv2.imread(img_path)
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
    # Criar cópias para remoção de canais
    img_sem_R = img_rgb.copy()
    img_sem_G = img_rgb.copy()
    img_sem_B = img_rgb.copy()
    
    # Remover canais (zerar)
    img_sem_R[:,:,0] = 0  # Remove vermelho
    img_sem_G[:,:,1] = 0  # Remove verde
    img_sem_B[:,:,2] = 0  # Remove azul
    
    # Mostrar comparação
    fig, axes = plt.subplots(2, 2, figsize=(12, 10))
    axes = axes.flatten()
    
    axes[0].imshow(img_rgb)
    axes[0].set_title("Original")
    axes[0].axis('off')
    
    axes[1].imshow(img_sem_R)
    axes[1].set_title("Sem Canal Vermelho (R=0)")
    axes[1].axis('off')
    
    axes[2].imshow(img_sem_G)
    axes[2].set_title("Sem Canal Verde (G=0)")
    axes[2].axis('off')
    
    axes[3].imshow(img_sem_B)
    axes[3].set_title("Sem Canal Azul (B=0)")
    axes[3].axis('off')
    
    # Converter de volta para BGR para salvar com OpenCV
    img_sem_R_bgr = cv2.cvtColor(img_sem_R, cv2.COLOR_RGB2BGR)
    img_sem_G_bgr = cv2.cvtColor(img_sem_G, cv2.COLOR_RGB2BGR)
    img_sem_B_bgr = cv2.cvtColor(img_sem_B, cv2.COLOR_RGB2BGR)
    
    # Salvar
    cv2.imwrite("resultados/ex4_sem_vermelho.jpg", img_sem_R_bgr)
    cv2.imwrite("resultados/ex4_sem_verde.jpg", img_sem_G_bgr)
    cv2.imwrite("resultados/ex4_sem_azul.jpg", img_sem_B_bgr)
    
    plt.tight_layout()
    plt.savefig("resultados/ex4_comparacao_canais.png")
    plt.show()
    
    print("Salvas: sem_vermelho.jpg, sem_verde.jpg, sem_azul.jpg")

def exercicio_5_escala_cinza(img_path):
    """
    Exercício 5 - Escala de Cinza
    """
    print("\n=== EXERCÍCIO 5 - ESCALA DE CINZA ===")
    
    img = cv2.imread(img_path)
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
    # Converter para escala de cinza
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # Mostrar comparação
    fig, axes = plt.subplots(1, 2, figsize=(12, 6))
    
    axes[0].imshow(img_rgb)
    axes[0].set_title("Imagem Original (Colorida)")
    axes[0].axis('off')
    
    axes[1].imshow(gray, cmap='gray')
    axes[1].set_title("Escala de Cinza")
    axes[1].axis('off')
    
    # Salvar
    cv2.imwrite("resultados/ex5_escala_cinza.jpg", gray)
    
    plt.tight_layout()
    plt.savefig("resultados/ex5_comparacao_cinza.png")
    plt.show()
    
    # Comparar tamanhos dos arquivos
    try:
        tamanho_original = os.path.getsize(img_path)
        tamanho_cinza = os.path.getsize("resultados/ex5_escala_cinza.jpg")
        
        print(f"Salva: escala_cinza.jpg")
        print(f"Tamanho arquivo original: {tamanho_original:,} bytes")
        print(f"Tamanho arquivo cinza: {tamanho_cinza:,} bytes")
        print(f"Redução: {((tamanho_original - tamanho_cinza) / tamanho_original * 100):.1f}%")
    except:
        print("Erro ao comparar tamanhos dos arquivos")

def main():
    """
    Função principal para executar todos os exercícios
    """
    # Caminho da imagem (altere conforme necessário)
    img_path = "sample_data/Imagem.jpg"  # Altere para o caminho da sua imagem
    
    # Verificar se a imagem existe
    if not os.path.exists(img_path):
        print(f"ATENÇÃO: Imagem não encontrada em {img_path}")
        print("Por favor, altere a variável 'img_path' para o caminho correto da sua imagem")
        return
    
    print("LISTA DE EXERCÍCIOS - PROCESSAMENTO DE IMAGENS")
    print("=" * 50)
    
    # Executar todos os exercícios
    exercicio_1_redimensionamento(img_path)
    exercicio_2_amostragem(img_path)
    exercicio_3_quantizacao(img_path)
    exercicio_4_remocao_canais(img_path)
    exercicio_5_escala_cinza(img_path)
    
    print("\n" + "=" * 50)
    print("TODOS OS EXERCÍCIOS CONCLUÍDOS!")
    print("Resultados salvos na pasta 'resultados/'")

# Executar o programa
if __name__ == "__main__":
    main()