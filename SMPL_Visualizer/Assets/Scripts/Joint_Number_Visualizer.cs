using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class Joint_Number_Visualizer : MonoBehaviour
{
    Vector3[,] joint_motions;
    GameObject[] text_gos;
    int frame_counter = 0;
    
    // Start is called before the first frame update
    void Start()
    {
        string fileData = System.IO.File.ReadAllText("Assets/Data/out_xyz.csv");
        string[] lines = fileData.Split("\n");
        joint_motions = new Vector3[lines.Length, lines[0].Split(",").Length / 3];

        for (int i = 0; i < lines.Length; i++){
            string[] frame_joints = lines[i].Split(",");
            for (int j = 0; j < frame_joints.Length; j += 3){
                Vector3 joint = new Vector3(float.Parse(frame_joints[j]), float.Parse(frame_joints[j + 1]), float.Parse(frame_joints[j + 2]));
                joint_motions[i, j / 3] = joint;
            }
        }

    text_gos = new GameObject[joint_motions.GetLength(1)];
    for (int i = 0; i < text_gos.Length; i++){
        GameObject new_go = new GameObject("joint_" + i.ToString());
        new_go.transform.SetParent(this.transform);
 
        TextMesh myText = new_go.AddComponent<TextMesh>();
        myText.text = i.ToString();
        myText.fontSize = 12;
        myText.font = Resources.GetBuiltinResource(typeof(Font), "Arial.ttf") as Font;


        text_gos[i] = new_go;
    }

    }

    // Update is called once per frame
    void Update()
    {
        for (int i = 0; i < text_gos.Length; i++){
            text_gos[i].transform.position = joint_motions[frame_counter, i];
        }

        Debug.Log(string.Join(", ", joint_motions[frame_counter, 5]));
        if (frame_counter < joint_motions.GetLength(0) - 1){
            frame_counter += 1;
        } else {
            frame_counter = 0;
        }
    }

//      GameObject text = new GameObject();
//  TextMesh t = text.AddComponent<TextMesh>();
//  t.text = "new text set";
//  t.fontSize = 30;
}
