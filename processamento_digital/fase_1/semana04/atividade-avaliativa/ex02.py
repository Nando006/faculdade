from matplotlib import pyplot;
from matplotlib import image;
import numpy;

imagem = 'semana04/atividade-avaliativa/download.jpg';

# Lendo a imagem em RGB
original = image.imread(imagem);

# Remover o canal azul B = 0
sem_azul = original.copy(); # Aqui estou criando uma cópia para não alterar a original
sem_azul[..., 2] = 0;

# Trocando os canais R e B = 0, 2
rb = original.copy();
rb[..., [0, 2]] = rb[..., [2, 0]]; # Aqui eu troco

# Reforçar o canal verde em 30%
reforcar = original.copy();
g = reforcar[..., 1].astype(numpy.float32); # Converter o tipo de dado (uint8) e o canal para float
g_aumentado = g * 1.3; # aumentando a intensidade em 30%
g_clipado = numpy.clip(g_aumentado, 0, 255); # Valores < 0 se tornam 0 e Valores > 255 se tornam 255.
reforcar[..., 1] = g_clipado.astype(original.dtype);

# Exibir os resultados
fig, axs = pyplot.subplots(1, 4, figsize=(20, 5));

axs[0].imshow(original);
axs[0].set_title('Imagem Original');
axs[0].axis('off');

axs[1].imshow(sem_azul);
axs[1].set_title('Sem canal azul');
axs[1].axis('off');

axs[2].imshow(rb);
axs[2].set_title('Canais R e B trocados');
axs[2].axis('off');

axs[3].imshow(reforcar);
axs[3].set_title('Canal verde +30%');
axs[3].axis('off');

pyplot.tight_layout();
pyplot.show();
