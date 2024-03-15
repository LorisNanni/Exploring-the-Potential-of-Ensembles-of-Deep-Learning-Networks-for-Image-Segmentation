# Data augmentation DA3
# change https://github.com/baiboat/HSNet/blob/main/utils/dataloader.py by the following transformations:


    if self.augmentations == 3:
            print('Using RandomRotation, RandomFlip, color changes')
            self.img_transform = transforms.Compose([
                transforms.RandomRotation(90),
                transforms.RandomVerticalFlip(p=0.5),
                transforms.RandomHorizontalFlip(p=0.5),
                transforms.RandomGrayscale(p=0.5),
                transforms.RandomInvert(p=0.5),
                transforms.RandomAutocontrast(p=0.2),
                transforms.RandomEqualize(p=0.2),
                transforms.Resize((self.trainsize, self.trainsize)),
                transforms.ToTensor(),
                transforms.Normalize([0.485, 0.456, 0.406],
                                     [0.229, 0.224, 0.225])])
            self.gt_transform = transforms.Compose([
                transforms.RandomRotation(90),
                transforms.RandomVerticalFlip(p=0.5),
                transforms.RandomHorizontalFlip(p=0.5),
                transforms.Resize((self.trainsize, self.trainsize)),
                transforms.ToTensor()])
