import discord
from discord.ext import commands
from discord.ui import Button, View

# 創建機器人客戶端
intents = discord.Intents.default()
intents.typing = False
intents.presences = False
intents.members = True  # 启用 GUILD_MEMBERS Intent
bot = commands.Bot(command_prefix='!', intents=intents)
intents.message_content = True # 機器人權限設置

#------------------------on ready-------------------------------
@bot.event
async def on_ready():
    print('Bot已登录')
    print(f'Logged in as {bot.user}!')
    slash = await bot.tree.sync()
    print(f"載入 {len(slash)} 個斜線指令")
    #機器人的遊戲狀態
    game = discord.Game('極光之域伺服器')
    #機器人的在線狀態
    await bot.change_presence(status=discord.Status.online, activity=game)

#------------------------身分組-------------------------------
@bot.event
async def on_raw_reaction_add(payload):
    # 替换成你的消息的ID
    message_id_1 = "1229709393495330816"#領取身分組 !
    message_id_2 = "1204282727478599702"#規則     !
    # 替换成你的表情符号的名称
    emoji_name_1 = "<:emoji_4:1229709932715311175>"#公告通知  !
    emoji_name_2 = "<:emoji_5:1229709994702934016>"#維修通知  !
    emoji_name_3 = "<:emoji_6:1229710094816514098>"#活動通知  !
    emoji_name_4 = "<:emoji_7:1229710130983993434>"#違規通知  !
    emoji_name_5 = "<:emoji_1:1204285219318792212>"#成員    !
    # 替换成你的身分组的ID
    role_id_str_1 = "1229705342909153280"#公告通知  !
    role_id_str_2 = "1229705433711775744"#維修通知  !
    role_id_str_3 = "1229704715726618665"#活動通知  !
    role_id_str_4 = "1230092531014963252"#違規通知  !
    role_id_str_5 = "1229705961204219925"#成員    !
    # 检查添加反应的消息是否为指定的消息
    #第一個 選擇通知add
    if str(payload.message_id) == message_id_1 and str(payload.emoji) == emoji_name_1:
        guild = bot.get_guild(payload.guild_id)
        if guild:
            member = guild.get_member(payload.user_id)
            if member:
                
                role = discord.utils.get(guild.roles, id=int(role_id_str_1))
                if role:
                    await member.add_roles(role)
                    print('add')
                    print(f"Added role {role.name} to {member.display_name}")
                    
                else:
                    print("Role not found.")
            else:
                print("Member not found.")
        else:
            print("Guild not found.")
    
    #第二個 選擇通知add
    if str(payload.message_id) == message_id_1 and str(payload.emoji) == emoji_name_2:
        guild = bot.get_guild(payload.guild_id)
        if guild:
            member = guild.get_member(payload.user_id)
            if member:
                
                role = discord.utils.get(guild.roles, id=int(role_id_str_2))
                if role:
                    await member.add_roles(role)
                    print('add')
                    print(f"Added role {role.name} to {member.display_name}")
                    
                else:
                    print("Role not found.")
            else:
                print("Member not found.")
        else:
            print("Guild not found.")

    #第三個 選擇通知add
    if str(payload.message_id) == message_id_1 and str(payload.emoji) == emoji_name_3:
        guild = bot.get_guild(payload.guild_id)
        if guild:
            member = guild.get_member(payload.user_id)
            if member:
                
                role = discord.utils.get(guild.roles, id=int(role_id_str_3))
                if role:
                    await member.add_roles(role)
                    print('add')
                    print(f"Added role {role.name} to {member.display_name}")
                    
                else:
                    print("Role not found.")
            else:
                print("Member not found.")
        else:
            print("Guild not found.")
            
    #第四個 選擇通知add
    if str(payload.message_id) == message_id_1 and str(payload.emoji) == emoji_name_4:
        guild = bot.get_guild(payload.guild_id)
        if guild:
            member = guild.get_member(payload.user_id)
            if member:
                
                role = discord.utils.get(guild.roles, id=int(role_id_str_4))
                if role:
                    await member.add_roles(role)
                    print('add')
                    print(f"Added role {role.name} to {member.display_name}")
                    
                else:
                    print("Role not found.")
            else:
                print("Member not found.")
        else:
            print("Guild not found.")
            
    #第五個 選擇通知add
    if str(payload.message_id) == message_id_2 and str(payload.emoji) == emoji_name_5:
        guild = bot.get_guild(payload.guild_id)
        if guild:
            member = guild.get_member(payload.user_id)
            if member:
                
                role = discord.utils.get(guild.roles, id=int(role_id_str_5))
                if role:
                    await member.add_roles(role)
                    print('add')
                    print(f"Added role {role.name} to {member.display_name}")
                    
                else:
                    print("Role not found.")
            else:
                print("Member not found.")
        else:
            print("Guild not found.")

@bot.event
async def on_raw_reaction_remove(payload):
    # 替换成你的消息的ID
    message_id_1 = "1229709393495330816"#領取身分組 !
    message_id_2 = "1204282727478599702"#規則     !
    # 替换成你的表情符号的名称
    emoji_name_1 = "<:emoji_4:1229709932715311175>"#公告通知  !
    emoji_name_2 = "<:emoji_5:1229709994702934016>"#維修通知  !
    emoji_name_3 = "<:emoji_6:1229710094816514098>"#活動通知  !
    emoji_name_4 = "<:emoji_7:1229710130983993434>"#違規通知  !
    emoji_name_5 = "<:emoji_1:1204285219318792212>"#成員    !
    # 替换成你的身分组的ID
    role_id_str_1 = "1229705342909153280"#公告通知  !
    role_id_str_2 = "1229705433711775744"#維修通知  !
    role_id_str_3 = "1229704715726618665"#活動通知  !
    role_id_str_4 = "1230092531014963252"#違規通知  !
    role_id_str_5 = "1229705961204219925"#成員    !
    # 检查添加反应的消息是否为指定的消息    
    #第一個 選擇通知del
    if str(payload.message_id) == message_id_1 and str(payload.emoji) == emoji_name_1:
        guild = bot.get_guild(payload.guild_id)
        if guild:
            member = guild.get_member(payload.user_id)
            if member:
                role = discord.utils.get(guild.roles, id=int(role_id_str_1))
                if role:
                    await member.remove_roles(role)
                    print('del')
                    print(f"Removed role {role.name} from {member.display_name}")
                    
                else:
                    print("Role not found.")
            else:
                print("Member not found.")
        else:
            print("Guild not found.")
            
    #第二個 選擇通知del
    if str(payload.message_id) == message_id_1 and str(payload.emoji) == emoji_name_2:
        guild = bot.get_guild(payload.guild_id)
        if guild:
            member = guild.get_member(payload.user_id)
            if member:
                
                role = discord.utils.get(guild.roles, id=int(role_id_str_2))
                if role:
                    await member.remove_roles(role)
                    print('del')
                    print(f"Removed role {role.name} from {member.display_name}")
                    
                else:
                    print("Role not found.")
            else:
                print("Member not found.")
        else:
            print("Guild not found.")

#第三個 選擇通知del
    if str(payload.message_id) == message_id_1 and str(payload.emoji) == emoji_name_3:
        guild = bot.get_guild(payload.guild_id)
        if guild:
            member = guild.get_member(payload.user_id)
            if member:
                
                role = discord.utils.get(guild.roles, id=int(role_id_str_3))
                if role:
                    await member.remove_roles(role)
                    print('del')
                    print(f"Removed role {role.name} from {member.display_name}")
                    
                else:
                    print("Role not found.")
            else:
                print("Member not found.")
        else:
            print("Guild not found.")

#第四個 選擇通知del
    if str(payload.message_id) == message_id_1 and str(payload.emoji) == emoji_name_4:
        guild = bot.get_guild(payload.guild_id)
        if guild:
            member = guild.get_member(payload.user_id)
            if member:
                
                role = discord.utils.get(guild.roles, id=int(role_id_str_4))
                if role:
                    await member.remove_roles(role)
                    print('del')
                    print(f"Removed role {role.name} from {member.display_name}")
                    
                else:
                    print("Role not found.")
            else:
                print("Member not found.")
        else:
            print("Guild not found.")

#第五個 選擇通知del
    if str(payload.message_id) == message_id_2 and str(payload.emoji) == emoji_name_5:
        guild = bot.get_guild(payload.guild_id)
        if guild:
            member = guild.get_member(payload.user_id)
            if member:
                
                role = discord.utils.get(guild.roles, id=int(role_id_str_5))
                if role:
                    await member.remove_roles(role)
                    print('del')
                    print(f"Removed role {role.name} from {member.display_name}")
                    
                else:
                    print("Role not found.")
            else:
                print("Member not found.")
        else:
            print("Guild not found.")

#
# 創建頻道並顯示關閉按鈕
@bot.tree.command(name="客服單", description="不要亂開吖")
async def add(interaction: discord.Interaction):
    if interaction.guild is None:
        await interaction.response.send_message("這不是你應該使用指令的地方", ephemeral=True)
        return
        
    guild = interaction.guild
    channel_name = interaction.user.name  # 使用者的暱稱
    existing_channel = discord.utils.get(guild.channels, name=channel_name)
    
    if not existing_channel:
        # 設定頻道權限
        overwrites = {
            guild.default_role: discord.PermissionOverwrite(read_messages=False),  # 其他人不可見
            interaction.user: discord.PermissionOverwrite(read_messages=True),     # 開單人可見
            guild.get_role(1304679684922933290): discord.PermissionOverwrite(read_messages=True)  # 管理員身份組可見
        }
        
        # 創建客服單頻道
        new_channel = await guild.create_text_channel(channel_name, overwrites=overwrites)
        
        # 設置「關閉」按鈕
        close_button = Button(label="關閉", style=discord.ButtonStyle.danger)
        
        # 按下「關閉」按鈕的回調函數
        async def close_button_callback(interaction: discord.Interaction):
            # 顯示「已要求關閉客服單」訊息並附加「確認」按鈕
            confirm_button = Button(label="確認", style=discord.ButtonStyle.danger)
            
            # 按下「確認」按鈕的回調函數
            async def confirm_button_callback(interaction: discord.Interaction):
                if new_channel:
                    await new_channel.delete()
                    print(f"{channel_name}的客服單已關閉")
                    try:
                        await interaction.response.send_message("客服單已關閉", ephemeral=True)
                    except discord.errors.NotFound:
                        # 頻道已被刪除，無需發送訊息
                        pass

            confirm_button.callback = confirm_button_callback
            
            confirm_view = View(timeout=None)  # 設置無限時長
            confirm_view.add_item(confirm_button)
            
            await interaction.response.send_message("已要求關閉客服單", view=confirm_view, ephemeral=True)

        close_button.callback = close_button_callback

        # 設置關閉按鈕的視圖，無超時限制
        view = View(timeout=None)  # 設置無限時長
        view.add_item(close_button)

        # 發送訊息並附加關閉按鈕
        await new_channel.send("客服單已開啟，請詳細說明問題", view=view)
        print(f"{channel_name}的客服單已開啟")
        await interaction.response.send_message(f"已創建新頻道： {new_channel.mention}", ephemeral=True)
    else:
        await interaction.response.send_message(f"你已有一個客服單了 #{existing_channel.mention}", ephemeral=True)

# 使用你的Bot token
bot.run("")
