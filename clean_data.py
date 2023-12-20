# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    clean_data.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: Dillon Koch <dillonk428@gmail.com>         +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/12/20 21:09:01 by Dillon Koch       #+#    #+#              #
#    Updated: 2023/12/20 21:35:33 by Dillon Koch      ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import pandas as pd
from abc import ABC, abstractmethod


class Clean_Data(ABC):
    def __init__(self, show):
        self.show = show

    @abstractmethod
    def clean_names(self):  # Top Level
        pass

    def run(self):  # Run
        raw = pd.read_csv(f"Data/{self.show}/raw.csv",
                          encoding='unicode_escape')
        raw = self.clean_names(raw)

        print('here')


class Clean_Office(Clean_Data):
    def __init__(self):
        pass

    def clean_names(self, df):  # Top Level
        """
        cleaning character names for typos and inconsistencies
        """
        df['speaker'] = df['speaker'].replace('Micheal', 'Michael')
        df['speaker'] = df['speaker'].replace('Robert California', 'Robert')
        df['speaker'] = df['speaker'].replace('David Wallace', 'David')
        return df


if __name__ == '__main__':
    shows = ['Office']
    for show in shows:
        x = Clean_Data(show)
        x.run()
