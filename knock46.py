import os
from collections import defaultdict

from knock41 import load_ai_ja_txt_parsed

if __name__ == '__main__':
    result = load_ai_ja_txt_parsed()

    out_path = 'knock46.txt'
    with open(out_path, 'w') as fw:
        for line in result:
            for chunk in line:
                if len(chunk.srcs) == 0:
                    continue
                if not chunk.has_verb():
                    continue
                base = chunk.get_verb(0).base
                particle_list = []
                src_surface_list = []
                for src in chunk.srcs:
                    if not line[src].has_particle():
                        continue
                    particle = line[src].get_particle(-1).surface
                    if particle not in particle_list:
                        particle_list.append(particle)
                    surface = line[src].surface
                    if particle not in src_surface_list:
                        src_surface_list.append(surface)

                fw.write(f'{base} {" ".join(particle_list)}  {" ".join(src_surface_list)}\n')
