import numpy as np

def evaluate_password_strength(model, char_to_index, max_length, password):
   
    # Convert password to sequence
    def password_to_sequence(password):
        return [char_to_index.get(char, 0) for char in password]
    
    # Prepare input
    seq = password_to_sequence(password)
    seq = np.pad(seq, (0, max_length - len(seq)), 'constant')
    seq = np.array([seq])
    
    # Get prediction
    strength_probs = model.predict(seq, verbose=0)[0]
    strength_class = np.argmax(strength_probs)
    strength_prob = strength_probs[strength_class]
    
    # Map numerical class to text label
    strength_labels = {
        0: "Weak",
        1: "Moderate",
        2: "Strong"
    }
    
    strength = strength_labels.get(strength_class, "Unknown")
    
    return strength, float(strength_prob)