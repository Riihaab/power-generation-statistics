from flask import Flask, request, jsonify
import pandas as pd

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False


@app.route('/top_annual_generation_plants', methods=['GET'])
def get_top_annual_generation_plants():
    limit = int(request.args.get('limit', '5'))
    print(f'*********lim*****{type(limit)}')
    data = pd.ExcelFile('egrid2016_data.xlsx')
    df = pd.read_excel(data, 'PLNT16')[['Plant annual net generation (MWh)', 'Plant name']]
    df.drop(index=df.index[0], axis=0, inplace=True)
    df.dropna(subset=["Plant annual net generation (MWh)"], inplace=True)
    df.sort_values(by='Plant annual net generation (MWh)', ascending=False, inplace=True)
    response = df.head(limit).to_dict('records')
    return jsonify(response)


@app.route('/get_annual_net_generation_by_state', methods=['GET'])
def get_annual_net_generation_by_state():
    state = request.args.get('state')
    data = pd.ExcelFile('egrid2016_data.xlsx')
    df = pd.read_excel(data, 'ST16')[['State abbreviation', 'State annual net generation (MWh)']]
    # df = df.loc[df['State abbreviation'] == state]
    df.drop(index=df.index[0], axis=0, inplace=True)
    df.dropna(subset=["State annual net generation (MWh)"], inplace=True)
    df['State annual net generation (MWh)'] = df['State annual net generation (MWh)'].abs()
    df['state annual net generation percentage'] = (df['State annual net generation (MWh)'] / df[
        'State annual net generation (MWh)'].sum()) * 100
    df['state annual net generation percentage'] = df['state annual net generation percentage'].apply(lambda x: round(x, 2))
    # df.sort_values(by='State annual net generation (MWh)', ascending=False, inplace=True)
    if state:
        df = df.loc[df['State abbreviation'] == state]
    response = df.to_dict('records')
    return jsonify(response)


if __name__ == '__main__':
    app.run(port=5000, debug=True)
