from settings import app, openai
from flask import request, render_template
from utils import retry_on_failure


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/analyze', methods=['POST'])
@retry_on_failure()
def analyze_text():
    '''Функция для анализа текста с помощью OpenAI GPT''' 

    prompt = request.form['text'] # Промпт для анализа
    selected_model = request.form['model'] # Выбранная модель GPT 

    app.logger.info(f"Model: {selected_model}, Prompt: {prompt}")
    
    # Отправляем промпт к выбранной модели
    response = openai.chat.completions.create(
        model=selected_model, 
        messages=[
            {"role": "system", "content": "You are a helpful AI travel assistant. You will give advices about places to visit"},
            {"role": "user", "content": prompt}
        ]
    )

    # Получаем результат
    analyzed_text = response.choices[0].message.content
    
    # Отправляем результат в шаблон
    return render_template('result.html', analyzed_text=analyzed_text)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
