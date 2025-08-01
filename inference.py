import torch
from torchvision import transforms
from PIL import Image
import sys

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

# Model
model = torch.nn.Sequential(
    torch.nn.Conv2d(3, 16, 3, stride=2),
    torch.nn.ReLU(),
    torch.nn.Flatten(),
    torch.nn.Linear(16*63*63, 2)
).to(device)

model.load_state_dict(torch.load("model/catdog_model.pt"))
model.eval()

# Transform
transform = transforms.Compose([
    transforms.Resize((128, 128)),
    transforms.ToTensor()
])

# Inference
img_path = sys.argv[1]
img = Image.open(img_path).convert('RGB')
img_tensor = transform(img).unsqueeze(0).to(device)
output = model(img_tensor)
_, predicted = torch.max(output.data, 1)

print(f"Predicted class: {'Dog' if predicted.item() else 'Cat'}")
