from flask import Blueprint, render_template, request, redirect , url_for, flash, jsonify
from flask_login import login_required, current_user
from .models import Data , User ,Stats, ShopItem
from . import db 

views = Blueprint('views', __name__)

    
@views.route('/game', methods=['GET', 'POST'])
@login_required
def game():
    level_data = User.query.filter_by(username = current_user.username).first()
    level = level_data.level
    level_updation = Stats.query.filter_by(username = current_user.username).first()
    level_updation.levels_cleared = level[0]
    inventory = (level_data.inventory).split()
    print(f"Current level : {level}")
    stage = Data.query.filter_by(level = level).first()
    if not stage:
        return render_template("subscribe.html")
    if stage.choices == 'RESTART':
        stats = Stats.query.filter_by(username=current_user.username).first()
        stats.deaths += 1
        db.session.commit()
    item = stage.item
    text = stage.text
    question  = stage.question
    choices = stage.choices
    if choices == 'RESTART' : 
        current_user.inventory = ""
    location = stage.location
    use = stage.use
    db.session.commit()
    return render_template("game.html", user=current_user , text=text , question=question , choices=choices , 
                           location=location , level=level , item=item , inventory=inventory , use=use)


@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    level = current_user.level
    return render_template("level_selection.html" , user = current_user , level=level)

@views.route('/update_level', methods=['POST'])
@login_required
def update_level():
    chosen_index = request.form.get('chosen_level')
    data = Data.query.filter_by(level = current_user.level).first()
    next = (data.next_level).split('$')
    print(f"next = {next}")
    print(f"chosen index = {chosen_index}")
    new_level = ''
    for i in range(1,len(next)+1):
        if str(i) == chosen_index:
            new_level = next[i-1]
    stats_update = Stats.query.filter_by(username=current_user.username).first()
    stats_update.coins += 10
    current_user.level = new_level
    db.session.commit()

    print(f"Level updated to {new_level}")
    return redirect(url_for('views.game'))

@views.route('/add_item', methods=['POST'])
@login_required
def add_item():
    add = request.form.get('add')  
    new_item = '$' + str(add)  
    inventory = current_user.inventory
    if new_item and new_item not in inventory:
        current_user.inventory += new_item
    db.session.commit()
    return redirect(url_for('views.game'))


@views.route('/stats')
@login_required
def stats():
    stats = Stats.query.filter_by(username=current_user.username).first()
    levels_cleared = stats.levels_cleared
    deaths = stats.deaths
    coins = stats.coins
    leaderboard = Stats.query.all()
    a=[]
    largest = leaderboard[0]
    
    while leaderboard:
        largest = leaderboard[0]
        for i in leaderboard:
            if i.coins > largest.coins:
                largest = i
        a.append(largest)
        leaderboard.remove(largest)
    return render_template("stats.html" , levels_cleared=levels_cleared , deaths=deaths , 
                           user=current_user,coins = coins , leaderboard = a )

@views.route('/shop')
def shop():
    shop_items = ShopItem.query.all()
    user = current_user
    item_added = request.args.get('item_added')
    return render_template("shop.html", user=user, shop_items=shop_items, item_added=item_added)


@views.route('/buy/<int:item_id>', methods=['POST'])
@login_required
def buy_item(item_id):
    username = current_user.username
    user=Stats.query.filter_by(username=username).first()
    shop_item = ShopItem.query.get(item_id)
  
    if shop_item and user.coins >= shop_item.cost:
        user.coins -= shop_item.cost
        current_user.inventory += f"${shop_item.name}"
        db.session.commit()
        return redirect(url_for('views.shop', item_added=shop_item.name))
    else:
        flash("You don't have enough coins or the item is not available!", category='error')
        return redirect(url_for('views.shop'))


@views.route('/use_item', methods=['POST'])
@login_required
def use_item():
    item_to_use = request.json.get('item')
    if item_to_use:
        current_user.inventory = current_user.inventory.replace(item_to_use, '').strip()
        db.session.commit()
        return jsonify({'message': f'{item_to_use} used successfully'}), 200
    else:
        return jsonify({'error': 'Item not provided'}), 400

@views.route('/subscribe', methods=['GET'])
@login_required
def subscribe():
    return render_template('subscribe.html')


@views.route('/thank_you')
@login_required
def thank_you():
   return render_template('thank_you.html')

