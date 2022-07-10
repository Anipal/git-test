import base64
from github import Github
from github import InputGitTreeElement

def push_git(load_n_test,csv_,src_path):
    user = "Anipal"
    password = "Anisha@Pal17!"
    g = Github(user,password)
    repo = g.get_user().get_repo('git-test') # repo name

    commit_message = 'python commit'
    master_ref = repo.get_git_ref('heads/master')
    master_sha = master_ref.object.sha
    base_tree = repo.get_git_tree(master_sha)

    element_list = list()
    entry = 'a.txt'
    # for i, entry in enumerate(file_list):
    with open(entry, "a+") as f:
        str_ = load_n_test+' , '+csv_+' , '+src_path
        f.write(str_)
        f.seek(0)
        data = f.read()
    # with open(entry) as input_file:
    #     data = input_file.read()
    file_name = entry.split('/')[-1]
    element = InputGitTreeElement(file_name, '100644', 'blob', data)
    element_list.append(element)

    tree = repo.create_git_tree(element_list, base_tree)
    parent = repo.get_git_commit(master_sha)
    commit = repo.create_git_commit(commit_message, tree, [parent])
    master_ref.edit(commit.sha)
