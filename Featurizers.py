

def baseline_featurize(sentence, position):
    token = sentence[position]
    features = {
        'bias': 1.0,
        'normalized token': token.lower(),
        '3 last letters':  token[-3:],
        '2 last letters':  token[-2:],
        'last letter':  token[-1:],
        'upper case?': token.isupper(),
        'numeric?':  token.isdigit()
    }

    if position > 0:
        last_token = sentence[position - 1]
        features.update({
            'normalized last token': last_token.lower(),
            'last token uppercase?':  last_token.isupper()
        })
    else:
        features['first token?'] = 1.0

    if position < len(sentence) - 1:
        next_token = sentence[position + 1]
        features.update({
            'normalized next token' : next_token.lower(),
            'next token uppercase?' : next_token.isupper(),
        })
    else:
        features['last token?'] = 1.0

    if position > 1:
        next_last_token = sentence[position - 2]
        features.update({
            'normalized next last token' : next_last_token.lower(),
            'next last token uppercase?' : next_last_token.isupper(),
        })

    if position < len(sentence) - 2:
        after_next_token = sentence[position + 2]
        features.update({
            'normalized after next token' : after_next_token.lower(),
            'after next token uppercase?' : after_next_token.isupper(),
        })

    return features


def baseline_featurize_no_bias(sentence, position):
    token = sentence[position]
    features = {
        'normalized token': token.lower(),
        '3 last letters':  token[-3:],
        '2 last letters':  token[-2:],
        'last letter':  token[-1:],
        'upper case?': token.isupper(),
        'numeric?':  token.isdigit()
    }

    if position > 0:
        last_token = sentence[position - 1]
        features.update({
            'normalized last token': last_token.lower(),
            'last token uppercase?':  last_token.isupper()
        })
    else:
        features['first token?'] = 1.0

    if position < len(sentence) - 1:
        next_token = sentence[position + 1]
        features.update({
            'normalized next token' : next_token.lower(),
            'next token uppercase?' : next_token.isupper(),
        })
    else:
        features['last token?'] = 1.0

    if position > 1:
        next_last_token = sentence[position - 2]
        features.update({
            'normalized next last token' : next_last_token.lower(),
            'next last token uppercase?' : next_last_token.isupper(),
        })

    if position < len(sentence) - 2:
        after_next_token = sentence[position + 2]
        features.update({
            'normalized after next token' : after_next_token.lower(),
            'after next token uppercase?' : after_next_token.isupper(),
        })

    return features

def minimal_featurize(sentence, position):
    token = sentence[position]
    features = {
        #'bias': 1.0,
        'normalized token': token.lower(),
        #'upper case?': token.isupper(),
    }
    return features


def minimal_featurize_bias(sentence, position):
    token = sentence[position]
    features = {
        'bias': 1.0,
        'normalized token': token.lower(),
        #'upper case?': token.isupper(),
    }
    return features

def minimal_featurize_zero_bias(sentence, position):
    token = sentence[position]
    features = {
        'bias': 0.0,
        'normalized token': token.lower(),
        #'upper case?': token.isupper(),
    }
    return features


def minimal_featurize_uppercase(sentence, position):
    token = sentence[position]
    features = {
        #'bias': 1.0,
        'normalized token': token.lower(),
        'upper case?': token.isupper(),
    }
    return features


def minimal_featurize_uppercase_bias(sentence, position):
    token = sentence[position]
    features = {
        'bias': 1.0,
        'normalized token': token.lower(),
        'upper case?': token.isupper(),
    }
    return features


def local_featurize_three(sentence, position):
    token = sentence[position]
    features = {
        'normalized token': token.lower(),
        '3 last letters':  token[-3:],
        '2 last letters':  token[-2:],
        'last letter':  token[-1:],
        'upper case?': token.isupper(),
        'numeric?':  token.isdigit()
    }
    return features

def local_featurize_two(sentence, position):
    token = sentence[position]
    features = {
        'normalized token': token.lower(),
        '2 last letters':  token[-2:],
        'last letter':  token[-1:],
        'upper case?': token.isupper(),
        'numeric?':  token.isdigit()
    }
    return features

def local_featurize_one(sentence, position):
    token = sentence[position]
    features = {
        'normalized token': token.lower(),
        'last letter':  token[-1:],
        'upper case?': token.isupper(),
        'numeric?':  token.isdigit()
    }
    return features

def local_featurize_zero(sentence, position):
    token = sentence[position]
    features = {
        'normalized token': token.lower(),
        'upper case?': token.isupper(),
        'numeric?':  token.isdigit()
    }
    return features

def local_featurize_four(sentence, position):
    token = sentence[position]
    features = {
        'normalized token': token.lower(),
        '4 last letters': token[-4:],
        '3 last letters':  token[-3:],
        '2 last letters':  token[-2:],
        'last letter':  token[-1:],
        'upper case?': token.isupper(),
        'numeric?':  token.isdigit()
    }
    return features

def local_featurize_five(sentence, position):
    token = sentence[position]
    features = {
        'normalized token': token.lower(),
        '5 last letters': token[-5:],
        '4 last letters': token[-4:],
        '3 last letters':  token[-3:],
        '2 last letters':  token[-2:],
        'last letter':  token[-1:],
        'upper case?': token.isupper(),
        'numeric?':  token.isdigit()
    }
    return features

def local_featurize_six(sentence, position):
    token = sentence[position]
    features = {
        'normalized token': token.lower(),
        '6 last letters': token[-6:],
        '5 last letters': token[-5:],
        '4 last letters': token[-4:],
        '3 last letters':  token[-3:],
        '2 last letters':  token[-2:],
        'last letter':  token[-1:],
        'upper case?': token.isupper(),
        'numeric?':  token.isdigit()
    }
    return features

def local_featurize_seven(sentence, position):
    token = sentence[position]
    features = {
        'normalized token': token.lower(),
        '7 last letters': token[-7:],
        '6 last letters': token[-6:],
        '5 last letters': token[-5:],
        '4 last letters': token[-4:],
        '3 last letters':  token[-3:],
        '2 last letters':  token[-2:],
        'last letter':  token[-1:],
        'upper case?': token.isupper(),
        'numeric?':  token.isdigit()
    }
    return features

def local_featurize_eight(sentence, position):
    token = sentence[position]
    features = {
        'normalized token': token.lower(),
        '8 last letters': token[-8:],
        '7 last letters': token[-7:],
        '6 last letters': token[-6:],
        '5 last letters': token[-5:],
        '4 last letters': token[-4:],
        '3 last letters':  token[-3:],
        '2 last letters':  token[-2:],
        'last letter':  token[-1:],
        'upper case?': token.isupper(),
        'numeric?':  token.isdigit()
    }
    return features

def local_featurize_nine(sentence, position):
    token = sentence[position]
    features = {
        'normalized token': token.lower(),
        '9 last letters': token[-9:],
        '8 last letters': token[-8:],
        '7 last letters': token[-7:],
        '6 last letters': token[-6:],
        '5 last letters': token[-5:],
        '4 last letters': token[-4:],
        '3 last letters':  token[-3:],
        '2 last letters':  token[-2:],
        'last letter':  token[-1:],
        'upper case?': token.isupper(),
        'numeric?':  token.isdigit()
    }
    return features

def local_featurize_skip(sentence, position):
    token = sentence[position]
    features = {
        'normalized token': token.lower(),
        '9 last letters': token[-9:],
        '7 last letters': token[-7:],
        '5 last letters': token[-5:],
        '3 last letters':  token[-3:],
        'last letter':  token[-1:],
        'upper case?': token.isupper(),
        'numeric?':  token.isdigit()
    }
    return features

def local_featurize_auto(sentence, position):
    token = sentence[position]
    features = {
        'normalized token': token.lower(),
        'upper case?': token.isupper(),
        'numeric?':  token.isdigit()
    }
    features.update({'%s last letters' % i : token[-i:] for i in range(1, 20)})
    return features

def local_featurize_auto_bias(sentence, position):
    token = sentence[position]
    features = {
        'bias' : 0.0,
        'normalized token': token.lower(),
        'upper case?': token.isupper(),
        'numeric?':  token.isdigit()
    }
    features.update({'%s last letters' % i : token[-i:] for i in range(1, 20)})
    return features


def neighbor_featurize_two(sentence, position):
    token = sentence[position]
    features = {
        'bias': 0.0,
        'normalized token': token.lower(),
        'upper case?': token.isupper(),
        'numeric?':  token.isdigit()
    }

    if position > 0:
        last_token = sentence[position - 1]
        features.update({
            'normalized last token': last_token.lower(),
            'last token uppercase?':  last_token.isupper()
        })
    else:
        features['first token?'] = 1.0

    if position < len(sentence) - 1:
        next_token = sentence[position + 1]
        features.update({
            'normalized next token' : next_token.lower(),
            'next token uppercase?' : next_token.isupper(),
        })
    else:
        features['last token?'] = 1.0

    if position > 1:
        next_last_token = sentence[position - 2]
        features.update({
            'normalized next last token' : next_last_token.lower(),
            'next last token uppercase?' : next_last_token.isupper(),
        })

    if position < len(sentence) - 2:
        after_next_token = sentence[position + 2]
        features.update({
            'normalized after next token' : after_next_token.lower(),
            'after next token uppercase?' : after_next_token.isupper(),
        })

    return features

def neighbor_featurize_three(sentence, position):
    token = sentence[position]
    features = {
        'bias': 0.0,
        'normalized token': token.lower(),
        'upper case?': token.isupper(),
        'numeric?':  token.isdigit()
    }

    if position > 0:
        last_token = sentence[position - 1]
        features.update({
            'normalized last token': last_token.lower(),
            'last token uppercase?':  last_token.isupper()
        })
    else:
        features['first token?'] = 1.0

    if position < len(sentence) - 1:
        next_token = sentence[position + 1]
        features.update({
            'normalized next token' : next_token.lower(),
            'next token uppercase?' : next_token.isupper(),
        })
    else:
        features['last token?'] = 1.0

    if position > 1:
        next_last_token = sentence[position - 2]
        features.update({
            'normalized next last token' : next_last_token.lower(),
            'next last token uppercase?' : next_last_token.isupper(),
        })

    if position < len(sentence) - 2:
        after_next_token = sentence[position + 2]
        features.update({
            'normalized after next token' : after_next_token.lower(),
            'after next token uppercase?' : after_next_token.isupper(),
        })

    if position > 2:
        next_next_last_token = sentence[position - 3]
        features.update({
            'normalized next next last token' : next_next_last_token.lower(),
            'next next last token uppercase?' : next_next_last_token.isupper(),
        })

    if position < len(sentence) - 3:
        after_after_next_token = sentence[position + 3]
        features.update({
            'normalized after after next token' : after_after_next_token.lower(),
            'after after next token uppercase?' : after_after_next_token.isupper(),
        })

    return features

def neighbor_featurize_four(sentence, position):
    token = sentence[position]
    features = {
        'bias': 0.0,
        'normalized token': token.lower(),
        'upper case?': token.isupper(),
        'numeric?':  token.isdigit()
    }

    if position > 0:
        last_token = sentence[position - 1]
        features.update({
            'normalized last token': last_token.lower(),
            'last token uppercase?':  last_token.isupper()
        })
    else:
        features['first token?'] = 1.0

    if position < len(sentence) - 1:
        next_token = sentence[position + 1]
        features.update({
            'normalized next token' : next_token.lower(),
            'next token uppercase?' : next_token.isupper(),
        })
    else:
        features['last token?'] = 1.0

    if position > 1:
        next_last_token = sentence[position - 2]
        features.update({
            'normalized next last token' : next_last_token.lower(),
            'next last token uppercase?' : next_last_token.isupper(),
        })

    if position < len(sentence) - 2:
        after_next_token = sentence[position + 2]
        features.update({
            'normalized after next token' : after_next_token.lower(),
            'after next token uppercase?' : after_next_token.isupper(),
        })

    if position > 2:
        next_next_last_token = sentence[position - 3]
        features.update({
            'normalized next next last token' : next_next_last_token.lower(),
            'next next last token uppercase?' : next_next_last_token.isupper(),
        })

    if position < len(sentence) - 3:
        after_after_next_token = sentence[position + 3]
        features.update({
            'normalized after after next token' : after_after_next_token.lower(),
            'after after next token uppercase?' : after_after_next_token.isupper(),
        })

    if position > 3:
        next_next_next_last_token = sentence[position - 4]
        features.update({
            'normalized next next next last token' : next_next_next_last_token.lower(),
            'next next next last token uppercase?' : next_next_next_last_token.isupper(),
        })

    if position < len(sentence) - 4:
        after_after_after_next_token = sentence[position + 4]
        features.update({
            'normalized after after after next token' : after_after_after_next_token.lower(),
            'after after after next token uppercase?' : after_after_after_next_token.isupper(),
        })

    return features

def combo_featurize(sentence, position):
    token = sentence[position]
    features = {
        'bias' : 0.0,
        'normalized token': token.lower(),
        'upper case?': token.isupper(),
        'numeric?':  token.isdigit()
    }
    features.update({'%s last letters' % i : token[-i:] for i in range(1, 20)})
    if position > 0:
        last_token = sentence[position - 1]
        features.update({
            'normalized last token': last_token.lower(),
            'last token uppercase?':  last_token.isupper()
        })
    else:
        features['first token?'] = 1.0

    if position < len(sentence) - 1:
        next_token = sentence[position + 1]
        features.update({
            'normalized next token' : next_token.lower(),
            'next token uppercase?' : next_token.isupper(),
        })
    else:
        features['last token?'] = 1.0

    if position > 1:
        next_last_token = sentence[position - 2]
        features.update({
            'normalized next last token' : next_last_token.lower(),
            'next last token uppercase?' : next_last_token.isupper(),
        })

    if position < len(sentence) - 2:
        after_next_token = sentence[position + 2]
        features.update({
            'normalized after next token' : after_next_token.lower(),
            'after next token uppercase?' : after_next_token.isupper(),
        })

    if position > 2:
        next_next_last_token = sentence[position - 3]
        features.update({
            'normalized next next last token' : next_next_last_token.lower(),
            'next next last token uppercase?' : next_next_last_token.isupper(),
        })

    if position < len(sentence) - 3:
        after_after_next_token = sentence[position + 3]
        features.update({
            'normalized after after next token' : after_after_next_token.lower(),
            'after after next token uppercase?' : after_after_next_token.isupper(),
        })

    if position > 3:
        next_next_next_last_token = sentence[position - 4]
        features.update({
            'normalized next next next last token' : next_next_next_last_token.lower(),
            'next next next last token uppercase?' : next_next_next_last_token.isupper(),
        })

    if position < len(sentence) - 4:
        after_after_after_next_token = sentence[position + 4]
        features.update({
            'normalized after after after next token' : after_after_after_next_token.lower(),
            'after after after next token uppercase?' : after_after_after_next_token.isupper(),
        })
    return features


def before_featurize(sentence, position):
    token = sentence[position]
    features = {
        'bias': 0.0,
        'normalized token': token.lower(),
        'upper case?': token.isupper(),
        'numeric?':  token.isdigit()
    }

    if position > 0:
        last_token = sentence[position - 1]
        features.update({
            'normalized last token': last_token.lower(),
            'last token uppercase?':  last_token.isupper()
        })
    else:
        features['first token?'] = 1.0



    if position > 1:
        next_last_token = sentence[position - 2]
        features.update({
            'normalized next last token' : next_last_token.lower(),
            'next last token uppercase?' : next_last_token.isupper(),
        })


    if position > 2:
        next_next_last_token = sentence[position - 3]
        features.update({
            'normalized next next last token' : next_next_last_token.lower(),
            'next next last token uppercase?' : next_next_last_token.isupper(),
        })



    if position > 3:
        next_next_next_last_token = sentence[position - 4]
        features.update({
            'normalized next next next last token' : next_next_next_last_token.lower(),
            'next next next last token uppercase?' : next_next_next_last_token.isupper(),
        })



    return features



def after_featurize(sentence, position):
    token = sentence[position]
    features = {
        'bias': 0.0,
        'normalized token': token.lower(),
        'upper case?': token.isupper(),
        'numeric?':  token.isdigit()
    }



    if position < len(sentence) - 1:
        next_token = sentence[position + 1]
        features.update({
            'normalized next token' : next_token.lower(),
            'next token uppercase?' : next_token.isupper(),
        })
    else:
        features['last token?'] = 1.0



    if position < len(sentence) - 2:
        after_next_token = sentence[position + 2]
        features.update({
            'normalized after next token' : after_next_token.lower(),
            'after next token uppercase?' : after_next_token.isupper(),
        })



    if position < len(sentence) - 3:
        after_after_next_token = sentence[position + 3]
        features.update({
            'normalized after after next token' : after_after_next_token.lower(),
            'after after next token uppercase?' : after_after_next_token.isupper(),
        })



    if position < len(sentence) - 4:
        after_after_after_next_token = sentence[position + 4]
        features.update({
            'normalized after after after next token' : after_after_after_next_token.lower(),
            'after after after next token uppercase?' : after_after_after_next_token.isupper(),
        })

    return features


def combo_featurize_auto(sentence, position):
    token = sentence[position]
    features = {
        'bias' : 0.0,
        'normalized token': token.lower(),
        'upper case?': token.isupper(),
        'numeric?':  token.isdigit()
    }
    features.update({'%s last letters' % i : token[-i:] for i in range(1, 4)})


    if position > 0:
        last_token = sentence[position - 1]
        features.update({
            'normalized last token': last_token.lower(),
            'last token uppercase?':  last_token.isupper()
        })
    else:
        features['first token?'] = 1.0

    if position < len(sentence) - 1:
        next_token = sentence[position + 1]
        features.update({
            'normalized next token' : next_token.lower(),
            'next token uppercase?' : next_token.isupper(),
        })
    else:
        features['last token?'] = 1.0

    for i in range(1, 4):
        if position > i:
            next_last_token = sentence[position - (i + 1)]
            features.update({
                'normalized %i last token' %i : next_last_token.lower(),
                '%i last token uppercase?' %i : next_last_token.isupper(),
            })

        if position < len(sentence) - (i + 1):
            after_next_token = sentence[position + (i + 1)]
            features.update({
                'normalized %i next token'%i : after_next_token.lower(),
                '%i next token uppercase?'%i : after_next_token.isupper(),
            })

    return features


def combo_featurize_auto_five(sentence, position):
    token = sentence[position]
    features = {
        'bias' : 0.0,
        'normalized token': token.lower(),
        'upper case?': token.isupper(),
        'numeric?':  token.isdigit()
    }
    features.update({'%s last letters' % i : token[-i:] for i in range(1, 20)})


    if position > 0:
        last_token = sentence[position - 1]
        features.update({
            'normalized last token': last_token.lower(),
            'last token uppercase?':  last_token.isupper()
        })
    else:
        features['first token?'] = 1.0

    if position < len(sentence) - 1:
        next_token = sentence[position + 1]
        features.update({
            'normalized next token' : next_token.lower(),
            'next token uppercase?' : next_token.isupper(),
        })
    else:
        features['last token?'] = 1.0

    for i in range(1, 5):
        if position > i:
            next_last_token = sentence[position - (i + 1)]
            features.update({
                'normalized %i last token' %i : next_last_token.lower(),
                '%i last token uppercase?' %i : next_last_token.isupper(),
            })

        if position < len(sentence) - (i + 1):
            after_next_token = sentence[position + (i + 1)]
            features.update({
                'normalized %i next token'%i : after_next_token.lower(),
                '%i next token uppercase?'%i : after_next_token.isupper(),
            })

    return features


def combo_featurize_auto_six(sentence, position):
    token = sentence[position]
    features = {
        'bias' : 0.0,
        'normalized token': token.lower(),
        'upper case?': token.isupper(),
        'numeric?':  token.isdigit()
    }
    features.update({'%s last letters' % i : token[-i:] for i in range(1, 20)})


    if position > 0:
        last_token = sentence[position - 1]
        features.update({
            'normalized last token': last_token.lower(),
            'last token uppercase?':  last_token.isupper()
        })
    else:
        features['first token?'] = 1.0

    if position < len(sentence) - 1:
        next_token = sentence[position + 1]
        features.update({
            'normalized next token' : next_token.lower(),
            'next token uppercase?' : next_token.isupper(),
        })
    else:
        features['last token?'] = 1.0

    for i in range(1, 6):
        if position > i:
            next_last_token = sentence[position - (i + 1)]
            features.update({
                'normalized %i last token' %i : next_last_token.lower(),
                '%i last token uppercase?' %i : next_last_token.isupper(),
            })

        if position < len(sentence) - (i + 1):
            after_next_token = sentence[position + (i + 1)]
            features.update({
                'normalized %i next token'%i : after_next_token.lower(),
                '%i next token uppercase?'%i : after_next_token.isupper(),
            })

    return features


def combo_featurize_auto_seven(sentence, position):
    token = sentence[position]
    features = {
        'bias' : 0.0,
        'normalized token': token.lower(),
        'upper case?': token.isupper(),
        'numeric?':  token.isdigit()
    }
    features.update({'%s last letters' % i : token[-i:] for i in range(1, 20)})


    if position > 0:
        last_token = sentence[position - 1]
        features.update({
            'normalized last token': last_token.lower(),
            'last token uppercase?':  last_token.isupper()
        })
    else:
        features['first token?'] = 1.0

    if position < len(sentence) - 1:
        next_token = sentence[position + 1]
        features.update({
            'normalized next token' : next_token.lower(),
            'next token uppercase?' : next_token.isupper(),
        })
    else:
        features['last token?'] = 1.0

    for i in range(1, 7):
        if position > i:
            next_last_token = sentence[position - (i + 1)]
            features.update({
                'normalized %i last token' %i : next_last_token.lower(),
                '%i last token uppercase?' %i : next_last_token.isupper(),
            })

        if position < len(sentence) - (i + 1):
            after_next_token = sentence[position + (i + 1)]
            features.update({
                'normalized %i next token'%i : after_next_token.lower(),
                '%i next token uppercase?'%i : after_next_token.isupper(),
            })

    return features


def combo_featurize_auto_eight(sentence, position):
    token = sentence[position]
    features = {
        'bias' : 0.0,
        'normalized token': token.lower(),
        'upper case?': token.isupper(),
        'numeric?':  token.isdigit()
    }
    features.update({'%s last letters' % i : token[-i:] for i in range(1, 20)})


    if position > 0:
        last_token = sentence[position - 1]
        features.update({
            'normalized last token': last_token.lower(),
            'last token uppercase?':  last_token.isupper()
        })
    else:
        features['first token?'] = 1.0

    if position < len(sentence) - 1:
        next_token = sentence[position + 1]
        features.update({
            'normalized next token' : next_token.lower(),
            'next token uppercase?' : next_token.isupper(),
        })
    else:
        features['last token?'] = 1.0

    for i in range(1, 8):
        if position > i:
            next_last_token = sentence[position - (i + 1)]
            features.update({
                'normalized %i last token' %i : next_last_token.lower(),
                '%i last token uppercase?' %i : next_last_token.isupper(),
            })

        if position < len(sentence) - (i + 1):
            after_next_token = sentence[position + (i + 1)]
            features.update({
                'normalized %i next token'%i : after_next_token.lower(),
                '%i next token uppercase?'%i : after_next_token.isupper(),
            })

    return features


def combo_featurize_auto_nine(sentence, position):
    token = sentence[position]
    features = {
        'bias' : 0.0,
        'normalized token': token.lower(),
        'upper case?': token.isupper(),
        'numeric?':  token.isdigit()
    }
    features.update({'%s last letters' % i : token[-i:] for i in range(1, 20)})


    if position > 0:
        last_token = sentence[position - 1]
        features.update({
            'normalized last token': last_token.lower(),
            'last token uppercase?':  last_token.isupper()
        })
    else:
        features['first token?'] = 1.0

    if position < len(sentence) - 1:
        next_token = sentence[position + 1]
        features.update({
            'normalized next token' : next_token.lower(),
            'next token uppercase?' : next_token.isupper(),
        })
    else:
        features['last token?'] = 1.0

    for i in range(1, 9):
        if position > i:
            next_last_token = sentence[position - (i + 1)]
            features.update({
                'normalized %i last token' %i : next_last_token.lower(),
                '%i last token uppercase?' %i : next_last_token.isupper(),
            })

        if position < len(sentence) - (i + 1):
            after_next_token = sentence[position + (i + 1)]
            features.update({
                'normalized %i next token'%i : after_next_token.lower(),
                '%i next token uppercase?'%i : after_next_token.isupper(),
            })

    return features
