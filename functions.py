def to_grayscale(image):
    """
    Converte uma imagem colorida (matriz 3D) para níveis de cinza.
    :param image: Matriz 3D (H x W x 3) representando a imagem.
    :return: Matriz 2D (H x W) representando a imagem em tons de cinza.
    """
    height = len(image)
    width = len(image[0])
    grayscale_image = [[0 for _ in range(width)] for _ in range(height)]
    
    for i in range(height):
        for j in range(width):
            r, g, b = image[i][j]
            # Fórmula ponderada para tons de cinza
            grayscale_value = int(0.299 * r + 0.587 * g + 0.114 * b)
            grayscale_image[i][j] = grayscale_value
    
    return grayscale_image

def binarize(image, threshold=128):
    """
    Binariza uma imagem em níveis de cinza.
    :param image: Matriz 2D (H x W) representando a imagem em tons de cinza.
    :param threshold: Limiar para binarização (default = 128).
    :return: Matriz 2D (H x W) representando a imagem binarizada.
    """
    height = len(image)
    width = len(image[0])
    binary_image = [[0 for _ in range(width)] for _ in range(height)]
    
    for i in range(height):
        for j in range(width):
            # Verifica o limiar e decide entre preto (0) e branco (255)
            binary_image[i][j] = 255 if image[i][j] >= threshold else 0
    
    return binary_image