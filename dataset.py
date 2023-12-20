# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    dataset.py                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: Dillon Koch <dillonk428@gmail.com>         +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/12/20 03:55:22 by Dillon Koch       #+#    #+#              #
#    Updated: 2023/12/20 05:54:29 by Dillon Koch      ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import pandas as pd
from torch.utils.data import Dataset


class QuoteDataset(Dataset):
    def __init__(self, show):
        self.show = show
        self.df = pd.read_csv(f"{self.show}.csv")

    def __len__(self):
        pass

    def __getitem__(self, idx):
        pass


if __name__ == '__main__':
    show = "Office"
    x = QuoteDataset(show)
    print(f"Length: {len(x)}")
    print(x.__getitem__(0))
