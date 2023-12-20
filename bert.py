# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    bert.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: Dillon Koch <dillonk428@gmail.com>         +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/12/20 04:16:32 by Dillon Koch       #+#    #+#              #
#    Updated: 2023/12/20 05:47:55 by Dillon Koch      ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from transformers import BertTokenizer, BertForSequenceClassification, AdamW
import pandas as pd
from tqdm import tqdm
from torch.utils.data import DataLoader


class Trainer:
    def __init__(self, show):
        self.show = show
        self.characters_dict = None # TODO

        self.tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")
        self.model = BertForSequenceClassification.from_pretrained("bert-base-uncased", num_labels=self.num_labels)

        self.epochs = 10

    def run(self):
        for epoch in range(self.epochs):
            self.model.train()



if __name__ == '__main__':
    x = Trainer()
    x.run()