# -*- coding: utf-8 -*-
"""
Organize vocabulary from minecraft_image_links.json into basic/intermediate/advanced files.
Update Chinese translations and add missing phrases.
"""
import json
import os
import time
from typing import Dict, List, Optional, Set

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# File paths
IMAGE_LINKS_PATH = os.path.join(BASE_DIR, 'minecraft_image_links.json')
BASIC_PATH = os.path.join(BASE_DIR, 'minecraft_basic.json')
INTERMEDIATE_PATH = os.path.join(BASE_DIR, 'minecraft_intermediate.json')
ADVANCED_PATH = os.path.join(BASE_DIR, 'minecraft_advanced.json')

# Core translation mappings (using Unicode escapes)
WIKI_TRANSLATIONS = {
    'water': '\u6c34',  # ˮ
    'stone': '\u77f3\u5934',  # ʯͷ
    'dirt': '\u6ce5\u571f',  # ����
    'grass': '\u8349\u65b9\u5757',  # �ݷ���
    'wood': '\u6728\u5934',  # ľͷ
    'oak': '\u6a61\u6728',  # ��ľ
    'planks': '\u6728\u677f',  # ľ��
    'leaves': '\u6811\u53f6',  # ��Ҷ
    'sapling': '\u6811\u82d7',  # ����
    'cobblestone': '\u5706\u77f3',  # Բʯ
    'bedrock': '\u57fa\u5ca9',  # ����
    'sand': '\u6c99\u5b50',  # ɳ��
    'gravel': '\u6c99\u7802',  # ɳ��
    'coal': '\u7164\u70ad',  # ú̿
    'iron': '\u94c1\u9320',  # ����
    'gold': '\u91d1\u9320',  # ��
    'diamond': '\u94bb\u77f3',  # ��ʯ
    'emerald': '\u7eff\u5b9d\u77f3',  # �̱�ʯ
    'redstone': '\u7ea2\u77f3\u7c89',  # ��ʯ��
    'lapis': '\u9752\u91d1\u77f3',  # ���ʯ
    'quartz': '\u77f3\u82f1',  # ʯӢ
    'obsidian': '\u9ed1\u66dc\u77f3',  # ����ʯ
    'glass': '\u73bb\u7483',  # ����
    'torch': '\u706b\u628a',  # ���
    'chest': '\u7bb1\u5b50',  # ����
    'furnace': '\u7194\u7089',  # ��¯
    'crafting table': '\u5de5\u4f5c\u53f0',  # ����̨
    'bed': '\u5e8a',  # ��
    'door': '\u95e8',  # ��
    'stairs': '\u697c\u68af',  # ¥��
    'slab': '\u53f0\u9636',  # ̨��
    'fence': '\u6805\u680f',  # դ��
    'gate': '\u6805\u680f\u95e8',  # դ����
    'wool': '\u7f8a\u6bdb',  # ��ë
    'red': '\u7ea2\u8272',  # ��ɫ
    'blue': '\u84dd\u8272',  # ��ɫ
    'green': '\u7eff\u8272',  # ��ɫ
    'yellow': '\u9ec4\u8272',  # ��ɫ
    'white': '\u767d\u8272',  # ��ɫ
    'black': '\u9ed1\u8272',  # ��ɫ
    'orange': '\u6a59\u8272',  # ��ɫ
    'purple': '\u7d2b\u8272',  # ��ɫ
    'pink': '\u7c89\u7ea2\u8272',  # �ۺ�ɫ
    'gray': '\u7070\u8272',  # ��ɫ
    'brown': '\u68d5\u8272',  # ��ɫ
    'cyan': '\u9752\u8272',  # ��ɫ
    'lime': '\u9ec4\u7eff\u8272',  # ����ɫ
    'magenta': '\u54c1\u7ea2\u8272',  # Ʒ��ɫ
    'light blue': '\u6de1\u84dd\u8272',  # ����ɫ
    'light gray': '\u6de1\u7070\u8272',  # ����ɫ
    'apple': '\u82f9\u679c',  # ƻ��
    'bread': '\u9762\u5305',  # ���
    'wheat': '\u5c0f\u9ea6',  # С��
    'seeds': '\u79cd\u5b50',  # ����
    'pig': '\u732a',  # ��
    'cow': '\u725b',  # ţ
    'sheep': '\u7ef5\u7f8a',  # ����
    'chicken': '\u9e21',  # ��
    'zombie': '\u50f5\u5c38',  # ��ʬ
    'skeleton': '\u9ab7\u9ac5',  # ����
    'creeper': '\u82e6\u529b\u6015',  # ������
    'spider': '\u8718\u86db',  # ֩��
    'enderman': '\u672b\u5f71\u4eba',  # ĩӰ��
    'sword': '\u5251',  # ��
    'pickaxe': '\u9550',  # ��
    'axe': '\u65a7\u5b50',  # ����
    'shovel': '\u94f2\u5b50',  # ����
    'hoe': '\u9504\u5934',  # ��ͷ
    'bow': '\u5f13',  # ��
    'arrow': '\u7bad',  # ��
    'armor': '\u76d4\u7532',  # ����
    'helmet': '\u5934\u76d4',  # ͷ��
    'chestplate': '\u80f8\u7532',  # �ؼ�
    'leggings': '\u62a4\u817f',  # ����
    'boots': '\u9774\u5b50',  # ѥ��
    'shield': '\u76fe\u724c',  # ����
    'bucket': '\u6876',  # Ͱ
    'milk': '\u725b\u5976',  # ţ��
    'egg': '\u9e21\u86cb',  # ����
    'leather': '\u76ae\u9769',  # Ƥ��
    'feather': '\u7fbd\u6bdb',  # ��ë
    'string': '\u7ebf',  # ��
    'flint': '\u71e7\u77f3',  # ��ʯ
    'stick': '\u6728\u68cd',  # ľ��
    'bowl': '\u7897',  # ��
    'sugar': '\u7cd6',  # ��
    'paper': '\u7eb8',  # ֽ
    'book': '\u4e66',  # ��
    'flower': '\u82b1',  # ��
    'mushroom': '\u8611\u83c7',  # Ģ��
    'cactus': '\u4ed9\u4eba\u638c',  # ������
    'pumpkin': '\u5357\u74dc',  # �Ϲ�
    'melon': '\u897f\u74dc',  # ����
    'carrot': '\u80e1\u841d\u535c',  # ���ܲ�
    'potato': '\u9a6c\u94c3\u85af',  # ������
    'beetroot': '\u751c\u83dc\u6839',  # ��˸�
    'nether': '\u4e0b\u754c',  # �½�
    'end': '\u672b\u5730',  # ĩ��
    'portal': '\u4f20\u9001\u95e8',  # ������
    'dragon': '\u672b\u5f71\u9f99',  # ĩӰ��
    'wither': '\u51cb\u96f6',  # ����
    'elytra': '\u9798\u7fc5',  # �ʳ�
    'trident': '\u4e09\u53c9\u621f',  # �����
    'crossbow': '\u5f29',  # ��
    'totem': '\u4e0d\u6b7b\u56fe\u817e',  # ����ͼ��
    'beacon': '\u4fe1\u6807',  # �ű�
    'anvil': '\u94c1\u7827',  # ����
    'enchanting table': '\u9644\u9b54\u53f0',  # ��ħ̨
    'brewing stand': '\u917f\u9020\u53f0',  # ����̨
    'cauldron': '\u70bc\u836f\u9505',  # ��ҩ��
    'dispenser': '\u53d1\u5c04\u5668',  # ������
    'dropper': '\u6295\u63b7\u5668',  # Ͷ����
    'hopper': '\u6f0f\u6597',  # ©��
    'piston': '\u6d3b\u585e',  # ����
    'lever': '\u62c9\u6746',  # ����
    'button': '\u6309\u94ae',  # ��ť
    'pressure plate': '\u538b\u529b\u677f',  # ѹ����
    'trapdoor': '\u6d3b\u677f\u95e8',  # �����
    'note block': '\u97f3\u7b26\u76d2',  # ������
    'jukebox': '\u5531\u7247\u673a',  # ��Ƭ��
    'rail': '\u94c1\u8f68',  # ����
    'minecart': '\u77ff\u8f66',  # ��
    'boat': '\u8239',  # ��
    'compass': '\u6307\u5357\u9488',  # ָ����
    'clock': '\u65f6\u949f',  # ʱ��
    'painting': '\u753b',  # ��
    'sign': '\u544a\u793a\u724c',  # ��ʾ��
    'ladder': '\u68af\u5b50',  # ����
    'snow': '\u96ea',  # ѩ
    'ice': '\u51b0',  # ��
    'tnt': 'TNT',  # TNT
    'sponge': '\u6d77\u7ef5',  # ����
    'clay': '\u9ecf\u571f\u5757',  # �����
    'brick': '\u7816\u5757',  # ש��
    'sandstone': '\u7802\u5ca9',  # ɰ��
    'granite': '\u82b1\u5c97\u5ca9',  # ������
    'diorite': '\u95ea\u957f\u5ca9',  # ������
    'andesite': '\u5b89\u5c71\u5ca9',  # ��ɽ��
    'prismarine': '\u6d77\u6676\u77f3',  # ����ʯ
    'sea lantern': '\u6d77\u6676\u706f',  # ������
    'magma block': '\u5ca9\u6d46\u5757',  # �ҽ���
    'netherrack': '\u4e0b\u754c\u5ca9',  # �½���
    'soul sand': '\u7075\u9b42\u6c99',  # ���ɳ
    'glowstone': '\u8367\u77f3',  # ӫʯ
    'end stone': '\u672b\u5730\u77f3',  # ĩ��ʯ
    'purpur block': '\u7d2b\u73c0\u5757',  # �����
    'chorus fruit': '\u7d2b\u9882\u679c',  # ���̹�
    'shulker box': '\u6f5c\u5f71\u76d2',  # ǱӰ��
    'ender chest': '\u672b\u5f71\u7bb1',  # ĩӰ��
    'spawner': '\u5237\u602a\u7b3c',  # ˢ����
    'cobweb': '\u8718\u86db\u7f51',  # ֩����
    'vine': '\u85e4\u8513',  # ����
    'lily pad': '\u7761\u83b2',  # ˯��
    'kelp': '\u6d77\u5e26',  # ����
    'bamboo': '\u7af9\u5b50',  # ����
    'honey block': '\u8702\u871c\u5757',  # ���ۿ�
    'honeycomb block': '\u871c\u813e\u5757',  # ��Ƣ��
    'bee nest': '\u8702\u5de2',  # �䳲
    'beehive': '\u8702\u7bb1',  # ����
    'copper': '\u94dc\u5757',  # ͭ��
    'amethyst': '\u7d2b\u6c34\u6676\u5757',  # ��ˮ����
    'deepslate': '\u6df1\u677f\u5ca9',  # �����
    'dripstone': '\u6ef4\u6c34\u77f3\u5757',  # ��ˮʯ��
    'moss block': '\u82d4\u85d3\u5757',  # ̦޺��
    'azalea': '\u675c\u9e43\u82b1\u4e1b',  # �ž黨��
    'spore blossom': '\u5b62\u5b50\u82b1',  # ���ӻ�
    'glow lichen': '\u53d1\u5149\u5730\u8863',  # �������
    'sculk': '\u5e7d\u5321\u5757',  # �����
    'sculk sensor': '\u5e7d\u5321\u611f\u6d4b\u4f53',  # ����в���
    'sculk catalyst': '\u5e7d\u5321\u50ac\u53d1\u4f53',  # ����߷���
    'sculk shrieker': '\u5e7d\u5321\u5c16\u5578\u4f53',  # �����Х��
    'warden': '\u76d1\u5b88\u8005',  # ������
    'mangrove': '\u7ea2\u6811',  # ����
    'mud': '\u6ce5\u5df4',  # ���
    'frog': '\u9752\u86d9',  # ����
    'tadpole': '\u8713\u86aa',  # ���
    'allay': '\u6096\u7075',  # ����
    'goat': '\u5c71\u7f8a',  # ɽ��
    'axolotl': '\u7f8e\u897f\u87b5',  # �����
    'glow squid': '\u53d1\u5149\u9c7f\u9c7c',  # ��������
    'powder snow': '\u7ec6\u96ea',  # ϸѩ
    'spyglass': '\u671b\u8fdc\u955c',  # ��Զ��
    'bundle': '\u6536\u7eb3\u888b',  # ���ɴ�
    'candle': '\u8721\u70db',  # ����
    'lightning rod': '\u907f\u96f7\u9488',  # ������
    'respawn anchor': '\u91cd\u751f\u9524',  # ����ê
    'lodestone': '\u78c1\u77f3',  # ��ʯ
    'crying obsidian': '\u54ed\u6ce3\u7684\u9ed1\u66dc\u77f3',  # �����ĺ���ʯ
    'blackstone': '\u9ed1\u77f3',  # ��ʯ
    'basalt': '\u7384\u6b66\u5ca9',  # ������
    'soul soil': '\u7075\u9b42\u571f',  # �����
    'soul torch': '\u7075\u9b42\u706b\u628a',  # �����
    'soul lantern': '\u7075\u9b42\u706f\u7b3c',  # ������
    'soul campfire': '\u7075\u9b42\u8425\u706b',  # ���Ӫ��
    'crimson': '\u7eef\u7ea2',  # 糺�
    'warped': '\u8be1\u5f02',  # ����
    'nylium': '\u83cc\u5ca9',  # ����
    'fungus': '\u83cc',  # ��
    'roots': '\u83cc\u7d22',  # ����
    'stem': '\u83cc\u67c4',  # ����
    'hyphae': '\u83cc\u6838',  # ����
    'shroomlight': '\u83cc\u5149\u4f53',  # ������
    'weeping vines': '\u5782\u6cea\u85e4',  # ������
    'twisting vines': '\u7f20\u6028\u85e4',  # ��Թ��
    'nether sprouts': '\u4e0b\u754c\u82d7',  # �½���
    'nether wart': '\u4e0b\u754c\u75a3',  # �½���
    'piglin': '\u732a\u7075',  # ����
    'hoglin': '\u75a3\u732a\u517d',  # ������
    'strider': '\u7092\u8db3\u517d',  # ������
    'zoglin': '\u50f5\u5c38\u75a3\u732a\u517d',  # ��ʬ������
    'netherite': '\u4e0b\u754c\u5408\u91d1',  # �½�Ͻ�
    'ancient debris': '\u8fdc\u53e4\u6b8b\u9ab8',  # Զ�Ųк�
    'target': '\u6807\u9776',  # ���
    'smithing table': '\u953b\u9020\u53f0',  # ����̨
    'fletching table': '\u5236\u7bad\u53f0',  # �Ƽ�̨
    'cartography table': '\u5236\u56fe\u53f0',  # ��ͼ̨
    'grindstone': '\u7802\u8f6e',  # ɰ��
    'stonecutter': '\u5207\u77f3\u673a',  # ��ʯ��
    'loom': '\u7ec7\u5e03\u673a',  # ֯����
    'composter': '\u5806\u80a5\u7bb1',  # �ѷ���
    'barrel': '\u6728\u6876',  # ľͰ
    'smoker': '\u70df\u718f\u7089',  # ��Ѭ¯
    'blast furnace': '\u9ad8\u7089',  # ��¯
    'campfire': '\u8425\u706b',  # Ӫ��
    'lantern': '\u706f\u7b3c',  # ����
    'bell': '\u949f',  # ��
    'scaffolding': '\u811a\u624b\u67b6',  # ���ּ�
    'lectern': '\u8bb2\u53f0',  # ��̨
    'conduit': '\u6f6e\u6d8c\u6838\u5fc3',  # ��ӿ����
    'turtle egg': '\u6d77\u9f9f\u86cb',  # ���군
    'scute': '\u9cde\u7532',  # �ۼ�
    'phantom membrane': '\u5e7b\u7fc5\u819c',  # ����Ĥ
    'nautilus shell': '\u9e66\u9e49\u87ba\u58f3',  # �����ݿ�
    'heart of the sea': '\u6d77\u6d0b\u4e4b\u5fc3',  # ����֮��
    'dragon breath': '\u9f99\u606f',  # ��Ϣ
    'nether star': '\u4e0b\u754c\u4e4b\u661f',  # �½�֮��
    'end crystal': '\u672b\u5f71\u6c34\u6676',  # ĩӰˮ��
    'enchanted golden apple': '\u9644\u9b54\u91d1\u82f9\u679c',  # ��ħ��ƻ��
    'golden apple': '\u91d1\u82f9\u679c',  # ��ƻ��
    'golden carrot': '\u91d1\u80e1\u841d\u535c',  # ����ܲ�
    'glistering melon slice': '\u95ea\u70c1\u7684\u897f\u74dc\u7247',  # ��˸������Ƭ
    'honey bottle': '\u8702\u871c\u74f6',  # ����ƿ
    'suspicious stew': '\u8ff7\u4e4b\u7092\u83dc',  # ��֮����
    'sweet berries': '\u751c\u6d46\u679c',  # �𽬹�
    'glow berries': '\u53d1\u5149\u6d46\u679c',  # ���⽬��
    'dried kelp': '\u5e72\u6d77\u5e26',  # �ɺ���
    'potion': '\u836f\u6c34',  # ҩˮ
    'splash potion': '\u55b7\u6e85\u836f\u6c34',  # �罦ҩˮ
    'lingering potion': '\u6ede\u7559\u836f\u6c34',  # ����ҩˮ
    'tipped arrow': '\u836f\u7bad',  # ҩ��
    'spectral arrow': '\u5149\u7075\u7bad',  # �����
    'firework rocket': '\u70df\u82b1\u706b\u7bad',  # �̻����
    'firework star': '\u70df\u82b1\u4e4b\u661f',  # �̻�֮��
    'item frame': '\u7269\u54c1\u5c55\u793a\u6846',  # ��Ʒչʾ��
    'glow item frame': '\u53d1\u5149\u7269\u54c1\u5c55\u793a\u6846',  # ������Ʒչʾ��
    'lead': '\u62f4\u7ef3',  # ˩��
    'name tag': '\u547d\u540d\u724c',  # ������
    'saddle': '\u978d',  # ��
    'horse armor': '\u9a6c\u94e0',  # ����
    'music disc': '\u97f3\u4e50\u5531\u7247',  # ���ֳ�Ƭ
    'banner': '\u65d7\u5e1c',  # ����
    'banner pattern': '\u65d7\u5e1c\u56fe\u6848',  # ����ͼ��
    'dye': '\u67d3\u6599',  # Ⱦ��
    'ink sac': '\u58a8\u56ca',  # ī��
    'glow ink sac': '\u53d1\u5149\u58a8\u56ca',  # ����ī��
    'bone': '\u9aa8\u5934',  # ��ͷ
    'bone meal': '\u9aa8\u7c89',  # �Ƿ�
    'gunpowder': '\u706b\u836f',  # ��ҩ
    'blaze powder': '\u70c8\u7130\u7c89',  # �����
    'blaze rod': '\u70c8\u7130\u68d2',  # �����
    'ender pearl': '\u672b\u5f71\u73cd\u73e0',  # ĩӰ����
    'eye of ender': '\u672b\u5f71\u4e4b\u773c',  # ĩӰ֮��
    'ghast tear': '\u6076\u9b42\u6cea',  # �����
    'magma cream': '\u5ca9\u6d46\u818f',  # �ҽ���
    'slimeball': '\u9ecf\u6db2\u7403',  # �Һ��
    'prismarine shard': '\u6d77\u6676\u7247',  # ����Ƭ
    'prismarine crystals': '\u6d77\u6676\u7c92',  # ������
    'rabbit foot': '\u5154\u5b50\u811a',  # ���ӽ�
    'rabbit hide': '\u5154\u5b50\u76ae',  # ����Ƥ
    'spider eye': '\u8718\u86db\u773c',  # ֩����
    'fermented spider eye': '\u53d1\u9175\u8718\u86db\u773c',  # ����֩����
    'rotten flesh': '\u8150\u8089',  # ����
    'poisonous potato': '\u6bd2\u9a6c\u94c3\u85af',  # ��������
    'pufferfish': '\u6cb3\u8c5a',  # ����
    'tropical fish': '\u70ed\u5e26\u9c7c',  # �ȴ���
    'cod': '\u9ccd\u9c7c',  # ����
    'salmon': '\u9c9b\u9c7c',  # ����
    'cooked cod': '\u719f\u9ccd\u9c7c',  # ������
    'cooked salmon': '\u719f\u9c9b\u9c7c',  # ������
    'cooked chicken': '\u719f\u9e21\u8089',  # �켦��
    'cooked porkchop': '\u719f\u732a\u6392',  # ������
    'cooked beef': '\u725b\u6392',  # ţ��
    'cooked mutton': '\u719f\u7f8a\u8089',  # ������
    'cooked rabbit': '\u719f\u5154\u8089',  # ������
    'raw chicken': '\u751f\u9e21\u8089',  # ������
    'raw porkchop': '\u751f\u732a\u6392',  # ������
    'raw beef': '\u751f\u725b\u8089',  # ��ţ��
    'raw mutton': '\u751f\u7f8a\u8089',  # ������
    'raw rabbit': '\u751f\u5154\u8089',  # ������
    'mushroom stew': '\u8611\u83c7\u7172',  # Ģ����
    'rabbit stew': '\u5154\u8089\u7172',  # ������
    'beetroot soup': '\u751c\u83dc\u6c64',  # �����
    'cookie': '\u66f2\u5947\u997c\u5e72',  # �������
    'cake': '\u86cb\u7cd5',  # ����
    'pumpkin pie': '\u5357\u74dc\u6d3e',  # �Ϲ���
    'melon slice': '\u897f\u74dc\u7247',  # ����Ƭ
    'baked potato': '\u70e4\u9a6c\u94c3\u85af',  # ��������
    'charcoal': '\u6728\u70ad',  # ľ̿
    'coal block': '\u7164\u70ad\u5757',  # ú̿��
    'iron block': '\u94c1\u5757',  # ����
    'gold block': '\u91d1\u5757',  # ���
    'diamond block': '\u94bb\u77f3\u5757',  # ��ʯ��
    'emerald block': '\u7eff\u5b9d\u77f3\u5757',  # �̱�ʯ��
    'lapis block': '\u9752\u91d1\u77f3\u5757',  # ���ʯ��
    'redstone block': '\u7ea2\u77f3\u5757',  # ��ʯ��
    'quartz block': '\u77f3\u82f1\u5757',  # ʯӢ��
    'iron ore': '\u94c1\u77ff\u77f3',  # ����ʯ
    'gold ore': '\u91d1\u77ff\u77f3',  # ���ʯ
    'diamond ore': '\u94bb\u77f3\u77ff\u77f3',  # ��ʯ��ʯ
    'emerald ore': '\u7eff\u5b9d\u77f3\u77ff\u77f3',  # �̱�ʯ��ʯ
    'lapis ore': '\u9752\u91d1\u77f3\u77ff\u77f3',  # ���ʯ��ʯ
    'redstone ore': '\u7ea2\u77f3\u77ff\u77f3',  # ��ʯ��ʯ
    'coal ore': '\u7164\u77ff\u77f3',  # ú��ʯ
    'copper ore': '\u94dc\u77ff\u77f3',  # ͭ��ʯ
    'nether gold ore': '\u4e0b\u754c\u91d1\u77ff\u77f3',  # �½���ʯ
    'nether quartz ore': '\u4e0b\u754c\u77f3\u82f1\u77ff\u77f3',  # �½�ʯӢ��ʯ
    'raw iron': '\u7c97\u94c1',  # ����
    'raw gold': '\u7c97\u91d1',  # �ֽ�
    'raw copper': '\u7c97\u94dc',  # ��ͭ
    'iron ingot': '\u94c1\u9320',  # ����
    'gold ingot': '\u91d1\u9320',  # ��
    'copper ingot': '\u94dc\u9320',  # ͭ��
    'netherite ingot': '\u4e0b\u754c\u5408\u91d1\u9320',  # �½�Ͻ�
    'netherite scrap': '\u4e0b\u754c\u5408\u91d1\u788e\u7247',  # �½�Ͻ���Ƭ
    'iron nugget': '\u94c1\u7c92',  # ����
    'gold nugget': '\u91d1\u7c92',  # ����
    'redstone dust': '\u7ea2\u77f3\u7c89',  # ��ʯ��
    'glowstone dust': '\u8367\u77f3\u7c89',  # ӫʯ��
    'lapis lazuli': '\u9752\u91d1\u77f3',  # ���ʯ
    'nether quartz': '\u4e0b\u754c\u77f3\u82f1',  # �½�ʯӢ
    'echo shard': '\u56de\u58f0\u788e\u7247',  # ������Ƭ
    'disc fragment': '\u5531\u7247\u788e\u7247',  # ��Ƭ��Ƭ
    'wheat seeds': '\u5c0f\u9ea6\u79cd\u5b50',  # С������
    'pumpkin seeds': '\u5357\u74dc\u79cd\u5b50',  # �Ϲ�����
    'melon seeds': '\u897f\u74dc\u79cd\u5b50',  # ��������
    'beetroot seeds': '\u751c\u83dc\u79cd\u5b50',  # �������
    'cocoa beans': '\u53ef\u53ef\u8c46',  # �ɿɶ�
    'torchflower seeds': '\u706b\u628a\u82b1\u79cd\u5b50',  # ��ѻ�����
    'pitcher pod': '\u74f6\u5b50\u8349\u8c46\u8358',  # ƿ�Ӳݶ���
    'sugar cane': '\u7518\u8517',  # ����
    'chorus fruit': '\u7d2b\u9882\u679c',  # ���̹�
    'popped chorus fruit': '\u7206\u88c2\u7d2b\u9882\u679c',  # �������̹�
    'oak boat': '\u6a61\u6728\u8239',  # ��ľ��
    'spruce boat': '\u4e91\u6749\u8239',  # ��ɼ��
    'birch boat': '\u767d\u6866\u8239',  # ���봬
    'jungle boat': '\u4e1b\u6797\u8239',  # ���ִ�
    'acacia boat': '\u91d1\u5408\u6b22\u8239',  # ��ϻ���
    'dark oak boat': '\u6df1\u8272\u6a61\u6728\u8239',  # ��ɫ��ľ��
    'mangrove boat': '\u7ea2\u6811\u8239',  # ������
    'cherry boat': '\u6a31\u82b1\u8239',  # ӣ����
    'bamboo raft': '\u7af9\u7b4f',  # ��
    'oak chest boat': '\u6a61\u6728\u8fd0\u8f93\u8239',  # ��ľ���䴬
    'spruce chest boat': '\u4e91\u6749\u8fd0\u8f93\u8239',  # ��ɼ���䴬
    'birch chest boat': '\u767d\u6866\u8fd0\u8f93\u8239',  # �������䴬
    'jungle chest boat': '\u4e1b\u6797\u8fd0\u8f93\u8239',  # �������䴬
    'acacia chest boat': '\u91d1\u5408\u6b22\u8fd0\u8f93\u8239',  # ��ϻ����䴬
    'dark oak chest boat': '\u6df1\u8272\u6a61\u6728\u8fd0\u8f93\u8239',  # ��ɫ��ľ���䴬
    'mangrove chest boat': '\u7ea2\u6811\u8fd0\u8f53\u8239',  # �������䴬
    'cherry chest boat': '\u6a31\u82b1\u8fd0\u8f93\u8239',  # ӣ�����䴬
    'bamboo chest raft': '\u7af9\u8fd0\u8f93\u7b4f',  # �����䷤
    'minecart with chest': '\u8fd0\u8f93\u77ff\u8f66',  # �����
    'minecart with furnace': '\u52a8\u529b\u77ff\u8f66',  # ������
    'minecart with tnt': 'TNT\u77ff\u8f66',  # TNT��
    'minecart with hopper': '\u6f0f\u6597\u77ff\u8f66',  # ©����
    'minecart with spawner': '\u5237\u602a\u7b3c\u77ff\u8f66',  # ˢ������
    'minecart with command block': '\u547d\u4ee4\u65b9\u5757\u77ff\u8f66',  # ������
    'powered rail': '\u52a8\u529b\u94c1\u8f68',  # ��������
    'detector rail': '\u63a2\u6d4b\u94c1\u8f68',  # ̽������
    'activator rail': '\u6fc0\u6d3b\u94c1\u8f68',  # ��������
    'recovery compass': '\u590d\u82cf\u6307\u5357\u9488',  # ����ָ����
    'fishing rod': '\u9493\u9c7c\u7aff',  # �����
    'shears': '\u526a\u5200',  # ����
    'fire charge': '\u706b\u7130\u5f39',  # ���浯
    'glass bottle': '\u73bb\u7483\u74f6',  # ����ƿ
    'water bucket': '\u6c34\u6876',  # ˮͰ
    'lava bucket': '\u5ca9\u6d46\u6876',  # �ҽ�Ͱ
    'milk bucket': '\u725b\u5976\u6876',  # ţ��Ͱ
    'powder snow bucket': '\u7ec6\u96ea\u6876',  # ϸѩͰ
    'bucket of cod': '\u9ccd\u9c7c\u6876',  # ����Ͱ
    'bucket of salmon': '\u9c9b\u9c7c\u6876',  # ����Ͱ
    'bucket of tropical fish': '\u70ed\u5e26\u9c7c\u6876',  # �ȴ���Ͱ
    'bucket of pufferfish': '\u6cb3\u8c5a\u6876',  # ����Ͱ
    'bucket of axolotl': '\u7f8e\u897f\u87b5\u6876',  # �����Ͱ
    'bucket of tadpole': '\u8713\u86aa\u6876',  # ���Ͱ
    'snowball': '\u96ea\u7403',  # ѩ��
    'ender eye': '\u672b\u5f71\u4e4b\u773c',  # ĩӰ֮��
    'written book': '\u4e66\u4e0e\u7b14',  # �����
    'book and quill': '\u4e66\u4e0e\u7b14',  # �����
    'enchanted book': '\u9644\u9b54\u4e66',  # ��ħ��
    'knowledge book': '\u77e5\u8bc6\u4e4b\u4e66',  # ֪ʶ֮��
    'writable book': '\u53ef\u5199\u4e66',  # ��д��
    'map': '\u5730\u56fe',  # ��ͼ
    'empty map': '\u7a7a\u5730\u56fe',  # �յ�ͼ
    'filled map': '\u5df2\u7ed8\u5236\u7684\u5730\u56fe',  # �ѻ��Ƶĵ�ͼ
    'explorer map': '\u63a2\u9669\u5bb6\u5730\u56fe',  # ̽�ռҵ�ͼ
    'ocean explorer map': '\u6d77\u6d0b\u63a2\u9669\u5bb6\u5730\u56fe',  # ����̽�ռҵ�ͼ
    'woodland explorer map': '\u6797\u5730\u63a2\u9669\u5bb6\u5730\u56fe',  # �ֵ�̽�ռҵ�ͼ
    'treasure map': '\u85cf\u5b9d\u56fe',  # �ر�ͼ
    'buried treasure map': '\u57cb\u85cf\u7684\u5b9d\u85cf\u5730\u56fe',  # ��صı��ص�ͼ
    'trial key': '\u8bd5\u70bc\u5ba4\u94a5\u5319',  # ������Կ��
    'ominous trial key': '\u4e0d\u7965\u8bd5\u70bc\u5ba4\u94a5\u5319',  # ����������Կ��
    'vault': '\u5b9d\u5e93',  # ����
    'ominous vault': '\u4e0d\u7965\u5b9d\u5e93',  # ���鱦��
    'trial spawner': '\u8bd5\u70bc\u5237\u602a\u7b3c',  # ����ˢ����
    'breeze': '\u5fae\u98ce',  # ΢��
    'wind charge': '\u98ce\u5f39',  # �絯
    'mace': '\u72fc\u7259\u68d2',  # ������
    'heavy core': '\u91cd\u6838',  # �غ�
    'flow armor trim': '\u6d41\u52a8\u76d4\u7532\u9970\u7eb9',  # ������������
    'bolt armor trim': '\u95ea\u7535\u76d4\u7532\u9970\u7eb9',  # �����������
    'flow banner pattern': '\u6d41\u52a8\u65d7\u5e1c\u56fe\u6848',  # ��������ͼ��
    'guster banner pattern': '\u72c2\u98ce\u65d7\u5e1c\u56fe\u6848',  # �������ͼ��
    'flow pottery sherd': '\u6d41\u52a8\u9676\u7247',  # ������Ƭ
    'guster pottery sherd': '\u72c2\u98ce\u9676\u7247',  # �����Ƭ
    'scrape pottery sherd': '\u522e\u64e6\u9676\u7247',  # �β���Ƭ
    'armadillo scute': '\u72b0\u5c71\u7532\u9cde\u7532',  # �����ۼ�
    'wolf armor': '\u72fc\u76d4\u7532',  # �ǿ���
    'armadillo spawn egg': '\u72b0\u5c71\u7532\u751f\u6210\u86cb',  # �������ɵ�
    'bogged spawn egg': '\u6cbc\u6cfd\u9ab7\u9ac5\u751f\u6210\u86cb',  # �����������ɵ�
    'breeze spawn egg': '\u5fae\u98ce\u751f\u6210\u86cb'  # ΢�����ɵ�
}

# Difficulty classification
BASIC_WORDS = {
    'stone', 'dirt', 'grass', 'wood', 'water', 'sand', 'gravel', 'coal', 'iron', 'oak', 'planks',
    'leaves', 'sapling', 'cobblestone', 'torch', 'chest', 'crafting', 'table', 'furnace',
    'pickaxe', 'sword', 'axe', 'shovel', 'hoe', 'stick', 'wool', 'bed', 'door', 'stairs',
    'slab', 'fence', 'gate', 'glass', 'flower', 'mushroom', 'apple', 'bread', 'wheat',
    'seeds', 'pig', 'cow', 'sheep', 'chicken', 'leather', 'feather', 'string', 'flint',
    'bucket', 'milk', 'egg', 'sugar', 'paper', 'book', 'granite', 'diorite', 'andesite',
    'bedrock', 'spruce', 'birch', 'jungle', 'acacia', 'sponge', 'dandelion', 'poppy',
    'orchid', 'tulip', 'daisy', 'cactus', 'clay', 'brick', 'sandstone', 'rail', 'minecart',
    'boat', 'compass', 'clock', 'painting', 'sign', 'ladder', 'snow', 'ice', 'pumpkin',
    'melon', 'carrot', 'potato', 'beetroot', 'kelp', 'bamboo', 'honey', 'honeycomb',
    'red', 'blue', 'green', 'yellow', 'white', 'black', 'orange', 'purple', 'pink',
    'gray', 'brown', 'cyan', 'lime', 'magenta', 'light'
}

INTERMEDIATE_WORDS = {
    'diamond', 'emerald', 'gold', 'redstone', 'lapis', 'quartz', 'obsidian', 'nether',
    'portal', 'blaze', 'ghast', 'zombie', 'skeleton', 'creeper', 'spider', 'enderman',
    'bow', 'arrow', 'armor', 'helmet', 'chestplate', 'leggings', 'boots', 'shield',
    'enchanting', 'anvil', 'brewing', 'potion', 'cauldron', 'dispenser', 'dropper',
    'hopper', 'piston', 'lever', 'button', 'pressure', 'plate', 'trapdoor', 'noteblock',
    'jukebox', 'beacon', 'conduit', 'prismarine', 'guardian', 'elder', 'sealantern',
    'magma', 'soul', 'blackstone', 'basalt', 'crimson', 'warped', 'shroomlight',
    'respawn', 'anchor', 'lodestone', 'netherite', 'ancient', 'debris', 'crying',
    'piglin', 'hoglin', 'strider', 'zoglin', 'target', 'copper', 'amethyst', 'deepslate',
    'dripstone', 'moss', 'azalea', 'dripleaf', 'spore', 'blossom', 'glow', 'lichen',
    'sculk', 'catalyst', 'sensor', 'shrieker', 'warden', 'mangrove', 'mud', 'frog',
    'tadpole', 'allay', 'goat', 'axolotl', 'squid', 'powder', 'telescope', 'bundle',
    'candle', 'lightning', 'rod', 'spyglass', 'tinted', 'tuff', 'calcite', 'pointed',
    'rooted', 'hanging', 'cave', 'lush', 'dripstone', 'powder', 'snow'
}

ADVANCED_WORDS = {
    'dragon', 'wither', 'elytra', 'shulker', 'chorus', 'purpur', 'end', 'crystal',
    'totem', 'undying', 'trident', 'crossbow', 'phantom', 'membrane', 'nautilus',
    'shell', 'heart', 'sea', 'scute', 'turtle', 'spectral', 'tipped', 'lingering',
    'splash', 'breath', 'nether', 'star', 'enchanted', 'golden', 'structure',
    'void', 'barrier', 'command', 'repeating', 'chain', 'jigsaw', 'debug',
    'knowledge', 'spawner', 'infested', 'silverfish', 'endermite', 'vex', 'evoker',
    'vindicator', 'pillager', 'ravager', 'witch', 'illusioner', 'giant', 'horse',
    'donkey', 'mule', 'llama', 'trader', 'wandering', 'fox', 'panda', 'bee',
    'polar', 'bear', 'dolphin', 'cod', 'salmon', 'tropical', 'fish', 'pufferfish',
    'bat', 'parrot', 'ocelot', 'cat', 'wolf', 'rabbit', 'mooshroom', 'golem',
    'villager', 'iron', 'snow', 'trial', 'vault', 'breeze', 'wind', 'charge',
    'mace', 'heavy', 'core', 'flow', 'bolt', 'guster', 'scrape', 'armadillo',
    'bogged', 'ominous'
}

def classify_difficulty(word: str) -> str:
    """Classify word difficulty based on game progression."""
    word_lower = word.lower()
    
    # Check for exact matches first
    if word_lower in BASIC_WORDS:
        return 'basic'
    elif word_lower in INTERMEDIATE_WORDS:
        return 'intermediate'
    elif word_lower in ADVANCED_WORDS:
        return 'advanced'
    
    # Check for partial matches
    for basic_word in BASIC_WORDS:
        if basic_word in word_lower or word_lower in basic_word:
            return 'basic'
    
    for intermediate_word in INTERMEDIATE_WORDS:
        if intermediate_word in word_lower or word_lower in intermediate_word:
            return 'intermediate'
    
    for advanced_word in ADVANCED_WORDS:
        if advanced_word in word_lower or word_lower in advanced_word:
            return 'advanced'
    
    # Default to intermediate if no match
    return 'intermediate'

def get_wiki_translation(word: str) -> Optional[str]:
    """Get translation from wiki mappings."""
    word_lower = word.lower().strip()
    return WIKI_TRANSLATIONS.get(word_lower)

def generate_phrase(word: str, chinese: str) -> tuple[str, str]:
    """Generate English phrase and Chinese translation."""
    word_lower = word.lower()
    
    # Determine category and generate phrase
    if any(tool in word_lower for tool in ['sword', 'pickaxe', 'axe', 'shovel', 'hoe']):
        phrase = f"use {word.lower()}"
        phrase_translation = f"\u4f7f\u7528{chinese}"  # ʹ��
    elif any(block in word_lower for block in ['stone', 'dirt', 'wood', 'planks', 'block']):
        phrase = f"mine {word.lower()}"
        phrase_translation = f"\u6316\u6398{chinese}"  # �ھ�
    elif any(food in word_lower for food in ['apple', 'bread', 'meat', 'fish', 'carrot']):
        phrase = f"eat {word.lower()}"
        phrase_translation = f"\u5403{chinese}"  # ��
    elif any(animal in word_lower for animal in ['pig', 'cow', 'sheep', 'chicken']):
        phrase = f"{word.lower()} farm"
        phrase_translation = f"{chinese}\u519c\u573a"  # ũ��
    elif any(color in word_lower for color in ['red', 'blue', 'green', 'yellow', 'white', 'black']):
        phrase = f"{word.lower()} wool"
        phrase_translation = f"{chinese}\u7f8a\u6bdb"  # ��ë
    else:
        phrase = f"find {word.lower()}"
        phrase_translation = f"\u627e\u5230{chinese}"  # �ҵ�
    
    return phrase, phrase_translation

def load_existing_words(file_path: str) -> Set[str]:
    """Load existing words from a vocabulary file."""
    existing_words = set()
    if os.path.exists(file_path):
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                for item in data:
                    existing_words.add(item.get('word', '').lower())
        except Exception as e:
            print(f"Error loading {file_path}: {e}")
    return existing_words

def process_vocabulary_entry(entry: dict) -> dict:
    """Process a single vocabulary entry."""
    word = entry.get('word', '').strip()
    if not word or word == '\u82f1\u6587\u540d\u79f0':  # Ӣ������
        return None
    
    # Get or update Chinese translation
    chinese = entry.get('chinese', '')
    if not chinese or chinese == '??':
        wiki_translation = get_wiki_translation(word)
        if wiki_translation:
            chinese = wiki_translation
        else:
            # Fallback translation logic
            chinese = word  # Keep original if no translation found
    
    # Classify difficulty
    difficulty = classify_difficulty(word)
    
    # Generate or update phrases
    phrase = entry.get('phrase', '')
    phrase_translation = entry.get('phraseTranslation', '')
    
    if not phrase or phrase == '????' or not phrase_translation or phrase_translation == '????':
        generated_phrase, generated_phrase_translation = generate_phrase(word, chinese)
        if not phrase or phrase == '????':
            phrase = generated_phrase
        if not phrase_translation or phrase_translation == '????':
            phrase_translation = generated_phrase_translation
    
    # Determine category
    category = entry.get('category', '')
    if not category:
        word_lower = word.lower()
        if any(tool in word_lower for tool in ['sword', 'pickaxe', 'axe', 'shovel', 'hoe']):
            category = 'tool'
        elif any(block in word_lower for block in ['stone', 'dirt', 'wood', 'block']):
            category = 'block'
        elif any(food in word_lower for food in ['apple', 'bread', 'meat', 'fish']):
            category = 'food'
        elif any(animal in word_lower for animal in ['pig', 'cow', 'sheep', 'chicken']):
            category = 'animal'
        elif any(color in word_lower for color in ['red', 'blue', 'green', 'yellow', 'white', 'black']):
            category = 'color'
        else:
            category = 'item'
    
    # Build the processed entry
    processed_entry = {
        'word': word,
        'standardized': entry.get('standardized', word),
        'chinese': chinese,
        'phonetic': entry.get('phonetic', ''),
        'phrase': phrase,
        'phraseTranslation': phrase_translation,
        'difficulty': difficulty,
        'category': category,
        'imageURLs': entry.get('imageURLs', [])
    }
    
    return processed_entry

def organize_vocabulary():
    """Main function to organize vocabulary from minecraft_image_links.json."""
    print("Starting vocabulary organization...")
    
    # Load source data
    if not os.path.exists(IMAGE_LINKS_PATH):
        print(f"Source file not found: {IMAGE_LINKS_PATH}")
        return
    
    with open(IMAGE_LINKS_PATH, 'r', encoding='utf-8') as f:
        source_data = json.load(f)
    
    print(f"Loaded {len(source_data)} entries from source file")
    
    # Load existing vocabulary files
    existing_basic = load_existing_words(BASIC_PATH)
    existing_intermediate = load_existing_words(INTERMEDIATE_PATH)
    existing_advanced = load_existing_words(ADVANCED_PATH)
    
    print(f"Existing words - Basic: {len(existing_basic)}, Intermediate: {len(existing_intermediate)}, Advanced: {len(existing_advanced)}")
    
    # Process and categorize entries
    basic_entries = []
    intermediate_entries = []
    advanced_entries = []
    
    processed_count = 0
    skipped_count = 0
    
    for entry in source_data:
        processed_entry = process_vocabulary_entry(entry)
        if not processed_entry:
            skipped_count += 1
            continue
        
        word_lower = processed_entry['word'].lower()
        difficulty = processed_entry['difficulty']
        
        # Check if word already exists in target files
        if (word_lower in existing_basic or 
            word_lower in existing_intermediate or 
            word_lower in existing_advanced):
            continue
        
        # Add to appropriate category
        if difficulty == 'basic':
            basic_entries.append(processed_entry)
        elif difficulty == 'intermediate':
            intermediate_entries.append(processed_entry)
        else:  # advanced
            advanced_entries.append(processed_entry)
        
        processed_count += 1
    
    print(f"Processed {processed_count} new entries, skipped {skipped_count}")
    print(f"New entries - Basic: {len(basic_entries)}, Intermediate: {len(intermediate_entries)}, Advanced: {len(advanced_entries)}")
    
    # Load and update existing files
    def update_vocabulary_file(file_path: str, new_entries: List[dict]):
        if not new_entries:
            print(f"No new entries for {os.path.basename(file_path)}")
            return
        
        existing_data = []
        if os.path.exists(file_path):
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    existing_data = json.load(f)
            except Exception as e:
                print(f"Error loading {file_path}: {e}")
        
        # Combine and sort
        combined_data = existing_data + new_entries
        combined_data.sort(key=lambda x: x.get('word', '').lower())
        
        # Create backup
        if existing_data:
            backup_path = file_path.replace('.json', f'.backup.{int(time.time())}.json')
            with open(backup_path, 'w', encoding='utf-8') as f:
                json.dump(existing_data, f, ensure_ascii=False, indent=2)
            print(f"Backup created: {backup_path}")
        
        # Save updated file
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(combined_data, f, ensure_ascii=False, indent=2)
        
        print(f"Updated {os.path.basename(file_path)} with {len(new_entries)} new entries (total: {len(combined_data)})")
    
    # Update all vocabulary files
    update_vocabulary_file(BASIC_PATH, basic_entries)
    update_vocabulary_file(INTERMEDIATE_PATH, intermediate_entries)
    update_vocabulary_file(ADVANCED_PATH, advanced_entries)
    
    print("\nVocabulary organization completed!")
    print(f"Total new entries added: {len(basic_entries) + len(intermediate_entries) + len(advanced_entries)}")

if __name__ == '__main__':
    organize_vocabulary()