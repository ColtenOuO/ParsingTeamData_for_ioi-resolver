import json

class PersonalDataToTeamData:
    def __init__(self, file_path) -> None:
        self.file_path = file_path
        self.data = self.parse_json_file(file_path)

    def get_data(self):
        return self.data

    def parse_json_file(self, file_path):
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                data = json.load(file)
                return data
        except FileNotFoundError:
            print(f"Error: File {file_path} not found.")
            return None
        except json.JSONDecodeError as e:
            print(f"Error parsing JSON: {e}")
            return None

    def update_user_id(self, new_user_id_mapping):
        if 'solutions' in self.data:
            for solution_id, solution_data in self.data['solutions'].items():
                old_user_id = solution_data.get('user_id')
                if old_user_id in new_user_id_mapping:
                    solution_data['user_id'] = new_user_id_mapping[old_user_id]
        else:
            print("No 'solutions' key found in parsed data.")

    def update_users(self, name_to_team):
        if 'users' in self.data:
            updated_users = {}
            for user_id, user_data in self.data['users'].items():
                user_name = user_data['name']
                team_name = name_to_team.get(user_name)
                if team_name:
                    user_data['name'] = team_name
                    if team_name not in updated_users:
                        updated_users[team_name] = user_data
            self.data['users'] = updated_users
        else:
            print("No 'users' key found in parsed data.")

    def clear_users(self):
        if 'users' in self.data:
            self.data['users'] = {}
        else:
            print("No 'users' key found in parsed data.")

    def save_to_file(self):
        try:
            with open(self.file_path, 'w', encoding='utf-8') as file:
                json.dump(self.data, file, ensure_ascii=False, indent=4)
            print(f"Data successfully saved to {self.file_path}")
        except Exception as e:
            print(f"Error saving JSON to {self.file_path}: {e}")

team_data = {
    "乂煞氣a摳硬乂": ["blameazu.", "LarryHSU", "Eugene-373yhh"],
    "此生單推涼": ["hzzz", "210627", "Youtong0826"],
    "You know the rules and so do I (owo)b": ["peterwang1120", "M0usee"],
    "OWO": ["lionpeng1225", "benny0972"],
    "ychsi12": ["zica87", "RexYang"],
    "194303": ["qqwww", "onnnnn", "lzspriv"],
    "NullPointerException": ["Cheng0928", "YuDong0222", "ShiYu318"],
    "Omaewa mo sindeiru": ["Rayray0515", "Preslayer", "bohan_19"],
    "SME": ["E_A_ho", "stupienius", "Mark0131"],
    "jim": ["jim0812", "chas981214", "diesellin"],
    "ahedaisyallen": ["Aries_Aysid", "Allen0407", "windist"],
    "2147483647": ["peipeiyan", "JerryWU"],
    "116": ["zi_zhen", "Rianna_r", "hsu960919"],
    "我們可是低性能的喔": ["IamLazyLLL", "DariusLin"],
    "Hello world": ["rex980811", "Luc_Chang", "Bear0915"],
    "howtocode": ["bird9612", "summer99", "Ccakes"],
    
    "Cocalocastic": ["PikaQSoWeak", "Crbubble", "Penguin07"],
    "dannyboy20031204": ["dannyboy20031204", "bear1222"],
    "GreedySet": ["m3vu", "bibikowolf"],
    "Team name (English):": ["boss_zz", "maxbrucelenhihi", "liu_jason_"],
    "whale_island": ["grozasqbb97", "H030m0001"],
    "DADA is gay": ["Dada878", "NYCU_Chung", "winliu"],
    "我隊友小帳tourist": ["flightzz", "goodsmellmountainpeople", "yok939"],
    "glimps": ["aoggg", "CuteRay", "selachi"],
    "ionc_group": ["Koala2002", "zheyu"],
    "lovkeqingforever": ["95kylelin", "skotono", "164253"]
}

name_to_team = {}

for team, members in team_data.items():
    for member in members:
        name_to_team[member] = team

def get_team_by_member(name):
    return name_to_team.get(name, "Not found")

if __name__ == "__main__":
    file_path = 'contest.json'
    solve = PersonalDataToTeamData(file_path)
    parsed_data = solve.get_data()

    if parsed_data:
        print("Original JSON data:")
        print(json.dumps(parsed_data, indent=4, ensure_ascii=False))

        new_user_id_mapping = {user_id: get_team_by_member(user_id) for solution_id, solution_data in parsed_data['solutions'].items() if (user_id := solution_data.get('user_id'))}
        solve.update_user_id(new_user_id_mapping)
        solve.save_to_file()

        solve.update_users(name_to_team)
        solve.save_to_file()
        
        print("Updated JSON data:")
        solve2 = PersonalDataToTeamData(file_path)
        parsed_data = solve2.get_data()
        print(json.dumps(parsed_data, indent=4, ensure_ascii=False))
