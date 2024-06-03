from website import create_app , seed_data , shop_items

app = create_app()

if __name__ == '__main__':
    seed_data.populate_db()
    shop_items.populate_shop()
    app.run(debug=True)