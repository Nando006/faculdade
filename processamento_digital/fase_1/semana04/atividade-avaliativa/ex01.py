from matplotlib import pyplot;
from matplotlib import image;
import numpy;

# Aqui eu defino a imagem
imagem = 'semana04/atividade-avaliativa/download.jpg';

# Vou adicionar um try-except para o programa não quebrar caso não tenha a imagem
try:
  # Ler a imagem em RGB
  rgb = image.imread(imagem); # Carrega a imagem como um Array no formato (altura, largura, canais)

  # Aqui vou extrair os canais RGB
  r = rgb[..., 0];
  g = rgb[..., 1];
  b = rgb[..., 2];

  # Nesta parte vou exibir os canais em tons de cinza com título e sem eixos
  figura, axs = pyplot.subplots(1, 4, figsize=(16, 4));

  # Vou adicionar a imagem original para comparações
  axs[0].imshow(rgb);
  axs[0].set_title('Imagem Original RGB');
  axs[0].axis('off')

  # Canal (R)
  axs[1].imshow(r, cmap='gray');
  axs[1].set_title('Canal R (Vermelho)');
  axs[1].axis('off'); # Essa parte remove os eixos

  # Canal (G)
  axs[2].imshow(g, cmap='gray');
  axs[2].set_title('Canal G (Verde)');
  axs[2].axis('off');

  # Canal (B)
  axs[3].imshow(b, cmap='gray');
  axs[3].set_title('Canal B (Vermelho)');
  axs[3].axis('off');

  pyplot.tight_layout();
  pyplot.show();


except FileNotFoundError:
  print(f"Imagem não encontrado adicione uma ao projeto", {imagem});

