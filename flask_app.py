from flask import Flask, render_template, request
from diffie_hellman import diffie_hellman_key_exchange

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    error = None
    prime = 23
    base = 5
    private_key_a = ''
    private_key_b = ''

    if request.method == 'POST':
        try:
            # Get form data
            prime_input = request.form.get('prime', type=int)
            base_input = request.form.get('base', type=int)
            private_key_a_input = request.form.get('private_key_a', type=int)
            private_key_b_input = request.form.get('private_key_b', type=int)

            # Validate inputs
            if prime_input < 3:
                raise ValueError("Prime number P must be greater than or equal to 3.")
            if base_input < 2:
                raise ValueError("Base G must be greater than or equal to 2.")

            # Assign to variables or None
            private_key_a_val = private_key_a_input if private_key_a_input and private_key_a_input >= 2 else None
            private_key_b_val = private_key_b_input if private_key_b_input and private_key_b_input >= 2 else None

            # Perform Diffie-Hellman Key Exchange
            result = diffie_hellman_key_exchange(prime=prime_input, base=base_input, 
                                                private_key_a=private_key_a_val, 
                                                private_key_b=private_key_b_val)
            
            # Update default values for form
            prime = prime_input
            base = base_input
            private_key_a = result['private_key_a']
            private_key_b = result['private_key_b']

        except Exception as e:
            error = str(e)

    return render_template('index.html', result=result, error=error, prime=prime, base=base, 
                           private_key_a=private_key_a, private_key_b=private_key_b)

if __name__ == '__main__':
    app.run(debug=True)
