from flask import Flask, request, jsonify
from huggingface_hub import hf_hub_download
# import re
from PIL import Image
from flask_cors import CORS
import base64

from transformers import NougatProcessor, VisionEncoderDecoderModel
from pdf2image import convert_from_path
from datasets import load_dataset
import torch
from io import BytesIO

# from flask_restful import reqparse, Api, Resource

app = Flask(__name__)
CORS(app)
# api = Api(app)

# parser = reqparse.RequestParser()
# parser.add_argument('task')

# class Message(Resource):
#     def get(self):
#         return {'message': 'Hello World :)'}

# api.add_resource(Message, '/api/hello')

@app.route('/api', methods=['POST'])
def home():
    data = request.form['image']
    return jsonify({ "message": data })
    # if 'image' in data:
    # processor = NougatProcessor.from_pretrained("facebook/nougat-base")
    # model = VisionEncoderDecoderModel.from_pretrained("facebook/nougat-base")
    
    # device = "cuda" if torch.cuda.is_available() else "cpu"
    # model.to(device)

    # filepath = hf_hub_download(repo_id="hf-internal-testing/fixtures_docvqa", filename="nougat_paper.png", repo_type="dataset")
    # file = data['image']
    # image_data = file.read()
    # image = Image.open(BytesIO(image_data))

    # return jsonify({"message": "image" })
    # pixel_values = processor(image, return_tensors="pt").pixel_values

    # # GENERATE
    # outputs = model.generate(
    #     pixel_values.to(device),
    #     min_length=1,
    #     max_new_tokens=30,
    #     bad_words_ids=[[processor.tokenizer.unk_token_id]],
    # )

    # # OUTPUTS
    # sequence = processor.batch_decode(outputs, skip_special_tokens=True)[0]
    # sequence = processor.post_process_generation(sequence, fix_markdown=False)

    # return jsonify({"message": repr(sequence)})

if __name__ == '__main__':
    app.run(debug=True)
