# noinspection PyPackageRequirements
import torch


# noinspection PyUnresolvedReferences
def main():
    print('CUDA available:\t', torch.cuda.is_available())
    print('CUDA version:\t', torch.version.cuda)
    print('cuDNN enabled:\t', torch.backends.cudnn.enabled)
    print('cuDNN version:\t', torch.backends.cudnn.version())


if __name__ == '__main__':
    main()
