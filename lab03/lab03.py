# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    lab03.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: schongte <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/09/02 15:21:56 by schongte          #+#    #+#              #
#    Updated: 2022/09/02 15:47:51 by schongte         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import math

print(int(math.pi))
print(f"{math.pi:.4f}")
print(f"{math.pi:e}")


uni = input("pls enter a character: ")

print(f'The Unicode of \"{uni}\" is u{hex(ord(uni)).replace("0x", "").zfill(4)}')


a = input ()
b = input ()
c = input ()

print(f"The whole string is {(a+b+c).upper()}.")
